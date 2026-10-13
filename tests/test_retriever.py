from src.retriever import Retriever

def test_retriever_finds_vacation():
    r = Retriever()
    hits = r.search("сколько дней отпуска")
    assert hits[0]["doc_id"] == "vacation"

def test_retriever_finds_remote():
    r = Retriever()
    hits = r.search("удалённая работа")
    assert hits[0]["doc_id"] == "remote_work"
