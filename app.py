import streamlit as st
from src.rag import HRRAGBot

st.set_page_config(page_title="HRBP Chatbot", layout="wide")
st.title("🤖 HR Business Partner Chatbot")
st.caption("Задайте вопрос по политикам: отпуск, удалёнка, компенсации, больничный")

@st.cache_resource
def get_bot():
    return HRRAGBot()

bot = get_bot()

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Ваш вопрос:")
if st.button("Спросить") and query:
    resp = bot.answer(query)
    st.session_state.history.append((query, resp))

for q, r in st.session_state.history:
    st.markdown(f"**Вы:** {q}")
    st.markdown(f"**Бот:** {r['answer']}")
    if r["sources"]:
        st.caption(f"Источники: {', '.join(r['sources'])} · уверенность: {r.get('confidence', '—')}")
    st.divider()
