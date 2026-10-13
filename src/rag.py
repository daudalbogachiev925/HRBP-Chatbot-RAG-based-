from src.retriever import Retriever

class HRRAGBot:
    def __init__(self):
        self.retriever = Retriever()

    def answer(self, query):
        hits = self.retriever.search(query, top_k=2)
        if not hits or hits[0]["score"] < 0.05:
            return {"answer": "Не нашёл информации в политиках. Обратитесь к HRBP.",
                    "sources": []}
        context = "\n\n".join(h["text"] for h in hits)
        return {
            "answer": f"По вашим политикам:\n\n{context}",
            "sources": [h["doc_id"] for h in hits],
            "confidence": round(hits[0]["score"], 3),
        }
