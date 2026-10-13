from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.knowledge_base import load_documents

class Retriever:
    def __init__(self):
        self.docs = load_documents()
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform([d["text"] for d in self.docs])

    def search(self, query, top_k=2):
        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.matrix)[0]
        idx = sims.argsort()[::-1][:top_k]
        return [{"doc_id": self.docs[i]["id"],
                 "text": self.docs[i]["text"],
                 "score": float(sims[i])} for i in idx]
