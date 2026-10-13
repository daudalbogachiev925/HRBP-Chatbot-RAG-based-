from src.policies import POLICIES

def load_documents():
    return [{"id": k, "text": v.strip()} for k, v in POLICIES.items()]

def chunk_text(text, chunk_size=200, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk:
            chunks.append(chunk)
    return chunks
