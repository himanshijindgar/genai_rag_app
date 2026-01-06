# GenAI RAG App (FastAPI + HTML UI)

A portfolio-ready skeleton for a Retrieval Augmented Generation (RAG) app:

- FastAPI backend
- HTML+JS frontend
- Upload text files
- Ask questions
- Designed to integrate with:
  - OpenAI embeddings / chat models
  - Pinecone vector database

Currently, `RAGEngine` uses stub logic so it runs without external APIs.
You can wire in real OpenAI + Pinecone by:

- Installing `openai` and `pinecone-client`
- Uncommenting the relevant lines in `app/rag.py`
- Setting environment variables:

```bash
export OPENAI_API_KEY="sk-..."
export PINECONE_API_KEY="..."
export PINECONE_INDEX="your-index-name"
```

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000

## Deploy with Docker

- Use the included `Dockerfile`
- Expose port 8000
- Configure environment variables if using real APIs
