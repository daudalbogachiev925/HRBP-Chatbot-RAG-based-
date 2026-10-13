from fastapi import FastAPI
from pydantic import BaseModel
from src.rag import HRRAGBot

app = FastAPI(title="HRBP Chatbot")
bot = HRRAGBot()

class Query(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(q: Query):
    return bot.answer(q.text)
