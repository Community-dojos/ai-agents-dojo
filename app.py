"""Mini interface Streamlit de démonstration du dojo."""
import streamlit as st
from common.config import get_model

st.set_page_config(page_title="AI Agents Dojo", page_icon="🤖")
st.title("AI Agents Developer Dojo")
st.caption("Démonstrateur minimal — assistant de synthèse pédagogique")

question = st.text_area("Votre question", "Explique la différence entre LangChain et LangGraph.")
if st.button("Envoyer", type="primary"):
    try:
        with st.spinner("Le modèle réfléchit..."):
            response = get_model().invoke(question)
        st.markdown(response.content)
    except Exception as exc:
        st.error(str(exc))
