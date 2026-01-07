# 🤖 GenAI RAG Application (Architecture Demo)

A **Retrieval-Augmented Generation (RAG)** application built using **FastAPI** with a simple **HTML + JavaScript UI**, deployed publicly on **Render (Free Tier)**.

This project demonstrates the **complete RAG system architecture and workflow**, intentionally running in **demo / stub mode** to remain **100% free**, without paid API keys or subscriptions.

---

## 🌐 Live Demo (Public)

🔗 **https://genai-rag-app.onrender.com**

> ℹ️ This demo runs without OpenAI or Pinecone to avoid paid dependencies.

---

## 🎯 Purpose of This Project

The goal of this project is to demonstrate:

- How a real **GenAI RAG system is architected**
- How document ingestion pipelines work
- How query → retrieval → response flow is designed
- How GenAI systems are deployed publicly
- How AI systems can be built under **cost constraints**

This project focuses on **system design and integration**, not on API spending.

---

## ✨ Features

- Upload documents via UI
- Backend document ingestion pipeline
- Question-answer interface
- RAG workflow skeleton
- Public deployment
- Free-tier friendly design

---

## 🧰 Tech Stack

### Backend
- **FastAPI** — ASGI web framework
- **Python 3.11** — stable runtime
- **Uvicorn** — ASGI server

### Frontend
- HTML
- CSS
- Vanilla JavaScript
- Fetch API

### AI Stack (Demo Mode)
- Stubbed embeddings
- Stubbed vector retrieval
- Stubbed LLM response

---

## 🏗️ Project Structure
genai_rag_app/
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── rag.py # RAG engine (demo/stub)
│ └── init.py
├── templates/
│ └── index.html # UI
├── static/
│ └── styles.css
├── requirements.txt
├── runtime.txt # Python version pin
└── README.md


---

## 🧠 What is RAG? (Conceptual Overview)

Retrieval-Augmented Generation combines:
1. **Information Retrieval** (searching relevant documents)
2. **Language Models** (generating responses using retrieved context)

### Typical RAG Flow
1. Upload documents
2. Chunk documents into smaller pieces
3. Generate embeddings for each chunk
4. Store embeddings in a vector database
5. Embed the user query
6. Retrieve relevant chunks
7. Pass context + query to LLM
8. Generate final answer

---

## ⚠️ Why This Demo Does NOT Use Real AI APIs

To remain:
- 100% free
- No subscriptions
- No API keys
- No rate limits
- No billing risk

This app uses **stubbed logic** instead of:
- OpenAI embeddings
- OpenAI chat models
- Pinecone / Weaviate / FAISS

---

## 🧪 What the Demo Actually Does

- Accepts uploaded files
- Stores document content temporarily in memory
- Accepts user questions
- Returns a **demo response** to show pipeline flow

This allows:
- UI testing
- Backend testing
- Architecture demonstration
- Interview walkthroughs

---

## 🔒 Security & Cost Considerations

- No API keys exposed
- No paid services connected
- No persistent document storage
- Safe to share publicly

---

## 🚀 Deployment Details

- Deployed on **Render (Free Tier)**
- Uses **Uvicorn**
- Python runtime pinned using `runtime.txt`
- Start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT


---

## 🧠 Common Interview Questions (Answered)

### Is this a real RAG system?
Architecturally yes.  
Execution-wise, it runs in demo mode.

---

### Why not use OpenAI or Pinecone?
To demonstrate **design first**, without cost or dependency lock-in.

---

### How would you make this production-ready?
- Add OpenAI embeddings
- Use a vector DB (Pinecone / FAISS / Weaviate)
- Implement chunking & metadata filtering
- Add authentication & rate limiting
- Persist documents securely

---

### Why deploy a demo instead of full AI?
Recruiters evaluate:
- architecture
- integration points
- deployment skills
- reasoning under constraints

Not API spending.

---

## 🧪 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
Visit: http://127.0.0.1:8000
