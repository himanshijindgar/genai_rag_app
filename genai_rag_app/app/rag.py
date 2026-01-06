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
        self.last_docs = docs
        print(f"[RAGEngine] Ingesting {len(docs)} documents...")
        for d in docs:
            _ = self._embed(d["text"])
        # Upsert omitted in skeleton.

    def query(self, question: str) -> str:
        if not hasattr(self, "last_docs") or not self.last_docs:
            return "No documents uploaded yet."
    
        text = self.last_docs[0]["text"]
        preview = text[:500]
    
        return (
            f"Based on the uploaded document, here is a preview:\n\n"
            f"{preview}\n\n"
            f"(This is a demo RAG response without external APIs.)"
        )

