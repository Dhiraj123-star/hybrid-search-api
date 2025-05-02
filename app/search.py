import sqlite3
import numpy as np
import os
from dotenv import load_dotenv
from app.models import Document
from langchain_openai import OpenAIEmbeddings

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Set the OPENAI_API_KEY environment variable.")

embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

def hybrid_search(query: str, conn: sqlite3.Connection, semantic_weight=0.6, exact_weight=0.4, top_k=5):
    query_embedding = embedding_model.embed_query(query)
    results = []

    documents = Document.get_all_documents(conn)

    for doc in documents:
        sim_score = float(np.dot(query_embedding, doc.embedding) /
                          (np.linalg.norm(query_embedding) * np.linalg.norm(doc.embedding)))
        exact_score = 1.0 if query.lower() in doc.content.lower() else 0.0
        final_score = semantic_weight * sim_score + exact_weight * exact_score
        results.append((doc.content, final_score))

    seen = set()
    unique_results = []
    for content, score in results:
        if content not in seen:
            seen.add(content)
            unique_results.append((content, score))

    sorted_results = sorted(unique_results, key=lambda x: x[1], reverse=True)[:top_k]
    return [{"content": content, "score": round(score, 2)} for content, score in sorted_results]
