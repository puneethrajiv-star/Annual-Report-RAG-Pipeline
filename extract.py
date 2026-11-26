import json
import gc
from collections import Counter

import camelot
import chromadb
import pandas as pd
import pdfplumber
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# SETTINGS - change these to switch reports
from settings import (
    PDF_FILE, PDF_PAGES, COLLECTION_NAME, CHUNKS_FILE,
    MIN_PAGE_TEXT_CHARS, TABLE_SCORE_THRESHOLD,
)

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
text_chunks = []

with pdfplumber.open(PDF_FILE) as pdf:
    if PDF_PAGES:
        selected_pages = {
            page_number for part in PDF_PAGES.split(",")
            for page_number in range(*(
                (int(part.split("-")[0]), int(part.split("-")[-1]) + 1)
                if "-" in part else (int(part), int(part) + 1)
            ))
        }
    else:
        selected_pages = set()
        for page_number, page in enumerate(pdf.pages, start=1):
            if len(page.extract_text() or "") >= MIN_PAGE_TEXT_CHARS:
                selected_pages.add(page_number)
            page.flush_cache()

    for page_number, page in enumerate(pdf.pages, start=1):
        if page_number not in selected_pages:
            continue
        table_boxes = [t.bbox for t in page.find_tables()]

        def not_in_table(obj):
            for x0, top, x1, bottom in table_boxes:
                if obj["x0"] >= x0 and obj["x1"] <= x1 and obj["top"] >= top and obj["bottom"] <= bottom:
                    return False
            return True

        text = page.filter(not_in_table).extract_text() or ""
        for chunk in splitter.split_text(text):
            text_chunks.append({"page": page_number, "type": "text", "content": chunk})
        page.flush_cache()

print(f"selected pages: {len(selected_pages)} of {len(pdf.pages)}")
print(f"text chunks: {len(text_chunks)}")

NUMBER = re.compile(r"(?<!\w)[$€£¥₹]?(?:\()?\d[\d,]*(?:\.\d+)?%?(?:\))?")
PURE_NUMBER = re.compile(r"^[\s$€£¥₹()\-–—+,\d.%]+$")


def cell_text(value):
    return str(value).strip()


def numeric_tokens(text):
    return [re.sub(r"\D", "", token) for token in NUMBER.findall(text)]


def is_value_cell(text):
    return bool(PURE_NUMBER.fullmatch(text) and re.search(r"\d", text))


def is_measure_cell(text):
    digits = re.sub(r"\D", "", text)
    return is_value_cell(text) and not re.fullmatch(r"(?:19|20)\d{2}", digits)


def is_data_row(row, column_count):
    cells = [cell_text(value) for value in row]
    has_label = any(re.search(r"[A-Za-z]", value) for value in cells)
    values = sum(is_measure_cell(value) for value in cells[1:])
    return has_label and values >= (1 if column_count == 2 else 2)


def first_data_row(df):
    for index, row in df.iterrows():
        if is_data_row(row, len(df.columns)):
            return index
    return None


def table_title_and_headers(df, data_start):
    title_rows, header_rows = [], []
    for _, row in df.iloc[:data_start].iterrows():
        cells = [cell_text(value) for value in row]
        nonempty = [value for value in cells if value]
        if len(nonempty) == 1:
            title_rows.append(nonempty[0])
        elif nonempty:
            header_rows.append(cells)

    headers = []
    for column in range(len(df.columns)):
        parts = []
        for row in header_rows:
            value = row[column]
            if value and value not in parts:
                parts.append(value)
        if parts:
            headers.append(" ".join(parts))
        elif column == 0:
            headers.append("Metric")
        else:
            headers.append(f"Value {chr(65 + column)}")
    return " ".join(title_rows), headers


def nearby_heading(page, table_bbox):
    x0, y1, x1, y2 = table_bbox
    table_top = page.height - y2
    lines = {}
    for word in page.extract_words():
        key = round(word["top"] / 3) * 3
        lines.setdefault(key, []).append(word)
    candidates = []
    for words in lines.values():
        words.sort(key=lambda word: word["x0"])
        line_bottom = max(word["bottom"] for word in words)
        text = " ".join(word["text"] for word in words)
        overlaps = max(word["x1"] for word in words) >= x0 and min(word["x0"] for word in words) <= x1
        if overlaps and 0 <= table_top - line_bottom <= 36 and len(words) <= 12:
            candidates.append((table_top - line_bottom, text))
    return min(candidates, default=(None, ""))[1]


def numbers_are_from_original(content, original_table_text):
    return Counter(numeric_tokens(content)) <= Counter(numeric_tokens(original_table_text))


def clamp_bbox(page, bbox):
    x0, top, x1, bottom = bbox
    bbox = (max(0, x0), max(0, top), min(page.width, x1), min(page.height, bottom))
    return bbox if bbox[0] < bbox[2] and bbox[1] < bbox[3] else None


def camelot_bbox(page, bbox):
    x0, y0, x1, y1 = bbox
    return clamp_bbox(page, (x0, page.height - y1, x1, page.height - y0))


def candidate_score(df):
    if df.empty or len(df.columns) < 2:
        return 0, None, "empty or one-column result"
    data_start = first_data_row(df)
    if data_start is None:
        return 0, None, "no structured numeric rows"
    data_rows = [row for _, row in df.iloc[data_start:].iterrows() if is_data_row(row, len(df.columns))]
    if len(data_rows) < 2:
        return 0, None, "fewer than two structured data rows"
    _, headers = table_title_and_headers(df, data_start)
    real_headers = [header for header in headers if header != "Metric" and not header.startswith("Value ")]
    header_quality = len(real_headers) / len(headers)
    values = [cell_text(value) for row in data_rows for value in list(row)[1:] if cell_text(value)]
    numeric_quality = sum(is_value_cell(value) for value in values) / len(values) if values else 0
    data_quality = 1 if len(df.columns) == 2 else len(data_rows) / len(df.iloc[data_start:])
    return round(0.4 * header_quality + 0.3 * numeric_quality + 0.3 * data_quality, 3), data_start, ""


def camelot_candidates(page_number, page, flavor, tables=None):
    candidates = []
    tables = tables if tables is not None else camelot.read_pdf(PDF_FILE, pages=str(page_number), flavor=flavor)
    for table in tables:
        bbox = camelot_bbox(page, table._bbox)
        if bbox:
            candidates.append({"df": table.df, "bbox": bbox, "strategy": flavor})
    return candidates


def pdfplumber_candidates(page):
    candidates = []
    for table in page.find_tables():
        bbox = clamp_bbox(page, table.bbox)
        if bbox:
            candidates.append({"df": pd.DataFrame(table.extract()), "bbox": bbox, "strategy": "pdfplumber"})
    return candidates


def overlaps(first, second):
    ax0, ay0, ax1, ay1 = first["bbox"]
    bx0, by0, bx1, by1 = second["bbox"]
    intersection = max(0, min(ax1, bx1) - max(ax0, bx0)) * max(0, min(ay1, by1) - max(ay0, by0))
    smaller = min((ax1 - ax0) * (ay1 - ay0), (bx1 - bx0) * (by1 - by0))
    return smaller and intersection / smaller >= 0.6


table_chunks, rejected_tables, accepted_tables = [], [], []
strategy_counts = Counter()
stream_by_page = {}
page_list = sorted(selected_pages)
for start in range(0, len(page_list), 10):
    stream_tables = camelot.read_pdf(PDF_FILE, pages=",".join(map(str, page_list[start:start + 10])), flavor="stream")
    for table in stream_tables:
        stream_by_page.setdefault(int(table.page), []).append(table)
    del stream_tables
    gc.collect()

with pdfplumber.open(PDF_FILE) as pdf:
    for page_number in sorted(selected_pages):
        page = pdf.pages[page_number - 1]
        candidates = camelot_candidates(page_number, page, "stream", stream_by_page.get(page_number, []))
        for candidate in candidates:
            candidate["score"], candidate["data_start"], candidate["reason"] = candidate_score(candidate["df"])

        needs_fallback = any(
            candidate["data_start"] is not None and candidate["score"] < TABLE_SCORE_THRESHOLD
            for candidate in candidates
        )
        if needs_fallback:
            for flavor in ("lattice",):
                candidates.extend(camelot_candidates(page_number, page, flavor))
            candidates.extend(pdfplumber_candidates(page))
            for candidate in candidates:
                if "score" not in candidate:
                    candidate["score"], candidate["data_start"], candidate["reason"] = candidate_score(candidate["df"])

        winners = []
        for candidate in sorted(candidates, key=lambda candidate: candidate["score"], reverse=True):
            if any(overlaps(candidate, winner) for winner in winners):
                continue
            winners.append(candidate)

        for candidate in winners:
            score = candidate["score"]
            if score < TABLE_SCORE_THRESHOLD:
                rejected_tables.append((page_number, candidate["strategy"], candidate["reason"] or "low table score"))
                continue

            crop_bbox = clamp_bbox(page, candidate["bbox"])
            if not crop_bbox:
                rejected_tables.append((page_number, candidate["strategy"], "empty table region"))
                continue
            original_table_text = page.crop(crop_bbox).extract_text() or ""
            if not original_table_text.strip():
                rejected_tables.append((page_number, candidate["strategy"], "empty table region"))
                continue

            df = candidate["df"]
            data_start = candidate["data_start"]
            title, headers = table_title_and_headers(df, data_start)
            caption = title or nearby_heading(page, (crop_bbox[0], page.height - crop_bbox[3], crop_bbox[2], page.height - crop_bbox[1]))
            if caption and not numbers_are_from_original(caption, original_table_text):
                caption = ""

            table_number = len(accepted_tables) + 1
            rows_added = 0
            for _, row in df.iloc[data_start:].iterrows():
                values = [cell_text(value) for value in row]
                if not is_data_row(values, len(df.columns)):
                    continue
                row_text = "; ".join(f"{header}: {value}" for header, value in zip(headers, values) if value)
                content = f"{caption} | {row_text}".strip(" |")
                if not numbers_are_from_original(content, original_table_text):
                    raise AssertionError(f"Numeric fidelity failed on page {page_number}, table {table_number}")
                table_chunks.append({
                    "page": page_number,
                    "type": "table",
                    "caption": caption,
                    "content": content,
                    "source": {"table": table_number, "row": int(row.name), "strategy": candidate["strategy"], "score": score},
                })
                rows_added += 1
            if rows_added:
                accepted_tables.append(candidate)
                strategy_counts[candidate["strategy"]] += 1
            else:
                rejected_tables.append((page_number, candidate["strategy"], "no numeric data rows"))

print(f"accepted tables by strategy: {dict(strategy_counts)}")
print(f"accepted chunks: {len(table_chunks)}; rejected candidates: {len(rejected_tables)}")
print(f"rejected reasons: {dict(Counter(reason for _, _, reason in rejected_tables))}")
print("numeric fidelity: passed")
for chunk in table_chunks[:5]:
    print(f"sample table page {chunk['page']} ({chunk['source']['strategy']}, {chunk['source']['score']}): {chunk['content']}")

all_chunks = text_chunks + table_chunks
texts = [c["content"] for c in all_chunks]
print("total chunks:", len(all_chunks))

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts, show_progress_bar=True)

client = chromadb.PersistentClient(path="chroma_db")
try:
    client.delete_collection(COLLECTION_NAME)
except Exception:
    pass
collection = client.create_collection(COLLECTION_NAME)

collection.add(
    ids=[str(i) for i in range(len(all_chunks))],
    embeddings=embeddings.tolist(),
    documents=texts,
    metadatas=[{"page": c["page"], "type": c["type"]} for c in all_chunks],
)

with open(CHUNKS_FILE, "w", encoding="utf-8") as file:
    json.dump(all_chunks, file, ensure_ascii=False, indent=2)

print("stored:", collection.count())
