from typing import List, Dict
import os

# In a real system, you would uncomment:
# import openai
# from pinecone import Pinecone, ServerlessSpec


class RAGEngine:
    # Simple RAG-style engine skeleton using OpenAI + Pinecone.
    # For portfolio/demo: runs without real API calls.
    def __init__(self, openai_api_key: str, pinecone_api_key: str, pinecone_index_name: str):
        self.openai_api_key = openai_api_key
        self.pinecone_api_key = pinecone_api_key
        self.index_name = pinecone_index_name
        # openai.api_key = self.openai_api_key
        # self.pc = Pinecone(api_key=self.pinecone_api_key)
        # self.index = self.pc.Index(self.index_name)

    def _embed(self, text: str) -> list:
        # Call embedding model and return vector (stub here for structure).
        # response = openai.Embedding.create(model="text-embedding-3-small", input=text)
        # return response["data"][0]["embedding"]
        # For demo: fixed-size zero vector
        return [0.0] * 10

    def ingest_documents(self, docs: List[Dict[str, str]]) -> None:
        # docs: list of {filename, text}.
        # Real flow:
        # - split to chunks
        # - embed each
        # - upsert to Pinecone
        print(f"[RAGEngine] Ingesting {len(docs)} documents...")
        for d in docs:
            _ = self._embed(d["text"])
        # Upsert omitted in skeleton.

    def query(self, question: str) -> str:
        # Real flow:
        # 1. Embed question
        # 2. Query Pinecone
        # 3. Compose prompt with retrieved context
        # 4. Call OpenAI chat model
        return f"Demo answer for: '{question}'. Wire this up to Pinecone + OpenAI for full RAG."
