from fastapi import FastAPI, Query, Depends
import sqlite3
from app.db import initialize_db
from app.search import hybrid_search

app = FastAPI()

# Initialize and seed database at startup
initialize_db()

def get_db():
    conn = sqlite3.connect("documents.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def read_root():
    return {
        "project": "Hybrid Search API",
        "description": "Combines exact keyword and semantic search using OpenAI embeddings.",
        "endpoints": {
            "/search": "Perform a hybrid search with your query parameter."
        },
        "status": "running"
    }


@app.get("/search")
def search(query: str = Query(..., min_length=1), conn: sqlite3.Connection = Depends(get_db)):
    results = hybrid_search(query, conn)
    return {"query": query, "results": results}
