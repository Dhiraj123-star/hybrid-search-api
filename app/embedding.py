import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Set the OPENAI_API_KEY environment variable.")

embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

def embed(text: str) -> list:
    return embedding_model.embed_query(text)
