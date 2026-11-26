# How It Works

This project turns an annual-report PDF into a searchable knowledge base for a retrieval-augmented generation (RAG) workflow.

`pdfplumber` reads the PDF's text layer. For narrative content, it identifies table regions first, removes those regions, and then extracts the remaining text. This prevents the same table text from being stored once as prose and again as a table.

`camelot` extracts tables. The extractor starts with Camelot's `stream` strategy, which uses whitespace alignment to infer columns. It scores each candidate using header quality, numeric-cell quality, and the share of rows that look like data. When an extracted candidate scores poorly, it retries with Camelot's `lattice` strategy and `pdfplumber` table extraction, then keeps the best non-overlapping candidate for that page.

`RecursiveCharacterTextSplitter` from LangChain breaks narrative text into 800-character chunks with 100 characters of overlap. The overlap helps preserve context at a chunk boundary.

`sentence-transformers` uses `all-MiniLM-L6-v2` to encode each text or table chunk as a 384-dimensional vector. Similar meaning produces nearby vectors, which makes semantic retrieval possible.

`chromadb` stores the vectors, original chunk text, and page/type metadata persistently in `chroma_db`. After `extract.py` has built a collection, `rag.py` can reuse it without parsing and embedding the PDF again.

`rag.py` embeds a user's question, retrieves the 10 nearest chunks from Chroma, builds a source-only context, and sends that context to Gemini for the final answer.

For tables, the numeric-fidelity check compares the numeric tokens in every emitted chunk with the original cropped PDF table region. If the output contains a number that is not in the source region, extraction stops with an assertion instead of silently changing financial data.

The extraction workflow has been regression-tested against two annual-report layouts: S&P Global FY2025 and Amazon FY2025. That check confirmed that the same pipeline can handle different page sizes, table structures, and report layouts while retaining source numbers.
