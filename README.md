# 🔍 hybrid-search-api

A lightweight, production-ready API that fuses exact keyword search and semantic similarity using OpenAI embeddings. Ideal for building fast, intelligent document search experiences with minimal infrastructure.

---

## ⚙️ Features

### 🔹 Hybrid Search Engine
Combines:
- **Exact search** for precise keyword matches using SQLite's full-text capabilities.
- **Semantic search** using vector similarity powered by OpenAI embeddings, enabling natural language queries and contextual matches.

### 🔹 FastAPI-Powered REST API
- Lightweight and high-performance web API built using [FastAPI](https://fastapi.tiangolo.com/).
- Automatically generates interactive Swagger and Redoc documentation.
- Clean endpoint structure for ease of integration.

### 🔹 Embedding-Enabled Document Store
- Stores content along with its embedding vector in an SQLite database.
- Accepts new documents via file ingestion (`documents.txt`).
- Handles embedding generation using OpenAI models in the background.

### 🔹 Auto-Bootstrap from File
- Automatically initializes and populates the database from a `documents.txt` file on first run.
- Ensures zero-manual setup for document ingestion.

### 🔹 Lightweight & Portable
- Uses SQLite for storage, keeping it dependency-free and easy to deploy anywhere.
- Can scale to other databases (e.g., PostgreSQL with pgvector) with minimal changes.

### 🔹 Environment-Configurable
- Secure OpenAI API key management using environment variables (`.env`).
- Decouples secrets from code.

---

## 🔌 Core Components

| File/Module         | Description                                      |
|---------------------|--------------------------------------------------|
| `main.py`           | FastAPI application with hybrid search endpoint  |
| `db.py`             | Auto-creates database and loads initial documents |
| `app/models.py`     | DB schema and logic for storing documents        |
| `app/search.py`     | Hybrid search logic (exact + semantic)           |
| `app/embedding.py`      | Embedding generation using OpenAI                |
| `documents.txt`     | Plaintext source file for document ingestion     |

---

## 🧪 Example Query Flow

1. User queries:  
   _"What are the benefits of semantic search?"_

2. Backend workflow:
   - Checks for exact keyword matches in stored content.
   - Simultaneously generates embedding of the query.
   - Computes cosine similarity between query embedding and document embeddings.
   - Combines both results with weighted logic to return the most relevant content.

3. Returns top matches via API.

---

## 🛡️ Security & Best Practices

- API key is never hard-coded — always use `.env`.
- Input is sanitized and limited to prevent injection or abuse.
- SQLite ensures simplicity for dev/prod parity.

---

Let me know if you want to include example API responses or sample document formatting from `documents.txt`.
