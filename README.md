# HRBP-Chatbot-RAG-based-
Чат-бот для HRBP на базе RAG (Retrieval-Augmented Generation): отвечает на вопросы по политикам, отвечает по данным сотрудников.
# HRBP Chatbot (RAG)

Чат-бот для HR Business Partner на TF-IDF retrieval + шаблонный RAG.
Отвечает на вопросы по политикам (отпуск, удалёнка, компенсации, больничный).

## Запуск
```bash
streamlit run app.py
```

## API
```bash
uvicorn api.main:app --reload
curl -X POST localhost:8000/ask -H "Content-Type: application/json" -d '{"text": "сколько дней отпуска?"}'
```
