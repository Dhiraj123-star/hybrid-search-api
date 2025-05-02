import sqlite3
import os
from app.models import Document

def initialize_db(db_path="documents.db", documents_file="documents.txt"):
    """
    Initializes the SQLite database by creating the documents table if it doesn't exist
    and populating it from a text file if empty.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # Create table if not exists
    c.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        embedding BLOB NOT NULL
    )
    """)
    conn.commit()

    # Populate DB if empty
    c.execute("SELECT COUNT(*) FROM documents")
    if c.fetchone()[0] == 0:
        print("Populating the database from documents.txt file...")
        populate_db_from_file(conn, documents_file)

    conn.commit()
    conn.close()  # ✅ Close the connection after initialization

def populate_db_from_file(conn, documents_file):
    """
    Populates the documents table from a .txt file line by line.
    """
    if os.path.exists(documents_file):
        with open(documents_file, 'r') as file:
            for line in file:
                content = line.strip()
                if content:
                    Document.add_document(conn, content)
