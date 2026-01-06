import os
from typing import List

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from .rag import RAGEngine

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "YOUR_PINECONE_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX", "your-index-name")

rag_engine = RAGEngine(
    openai_api_key=OPENAI_API_KEY,
    pinecone_api_key=PINECONE_API_KEY,
    pinecone_index_name=PINECONE_INDEX,
)

app = FastAPI(title="GenAI RAG App")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/ingest")
async def ingest(files: List[UploadFile] = File(...)):
    contents = []
    for f in files:
        text = (await f.read()).decode("utf-8", errors="ignore")
        contents.append({"filename": f.filename, "text": text})
    rag_engine.ingest_documents(contents)
    return {"detail": f"Ingested {len(contents)} file(s)."}


@app.post("/chat")
async def chat(query: str = Form(...)):
    answer = rag_engine.query(query)
    return {"answer": answer}
