import sqlite3
import numpy as np
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

class Document:
    def __init__(self, id, content, embedding):
        self.id = id
        self.content = content
        self.embedding = embedding

    @staticmethod
    def add_document(conn, content):
        # Generate embedding
        embedding = embedding_model.embed_query(content)

        # Convert embedding to blob
        embedding_blob = np.array(embedding, dtype=np.float32).tobytes()

        # Insert document and embedding into DB
        c = conn.cursor()
        c.execute("INSERT INTO documents (content, embedding) VALUES (?, ?)", (content, embedding_blob))
        conn.commit()

    @staticmethod
    def get_all_documents(conn):
        c = conn.cursor()
        c.execute("SELECT id, content, embedding FROM documents")
        rows = c.fetchall()

        # Convert each row into a Document object
        documents = []
        for row in rows:
            doc_id, content, embedding_blob = row
            embedding = np.frombuffer(embedding_blob, dtype=np.float32)
            documents.append(Document(doc_id, content, embedding))

        return documents
