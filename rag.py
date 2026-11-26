import json
import os

import chromadb
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from settings import COLLECTION_NAME, CHUNKS_FILE

with open(CHUNKS_FILE, encoding="utf-8") as file:
    all_chunks = json.load(file)

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection(COLLECTION_NAME)

model = SentenceTransformer("all-MiniLM-L6-v2")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model_llm = genai.GenerativeModel("gemini-3.5-flash")

while True:
    question = input("Question (or 'exit'): ").strip()
    if question.lower() == "exit":
        break

    q_vec = model.encode([question]).tolist()
    results = collection.query(query_embeddings=q_vec, n_results=10)

    context = "\n\n".join(
        [f"Page {m['page']} ({m['type']}): {d}"
         for d, m in zip(results["documents"][0], results["metadatas"][0])]
    )

    response = model_llm.generate_content(
        f"Answer based only on this context:\n\n{context}\n\nQuestion: {question}"
    )
    print(response.text)
