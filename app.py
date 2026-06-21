import streamlit as st

st.title("Document Q&A Bot using RAG")

st.write("This is a demonstration deployment for the RAG assignment.")

question = st.text_input("Ask a question")

if question:
st.write("Question:", question)
st.write("Answer generation logic would run here.")
