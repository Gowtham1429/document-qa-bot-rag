import streamlit as st

st.title("Document Q&A Bot using RAG")

st.write("This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline.")

question = st.text_input("Ask a question")

if question:
    st.write("Question:", question)
    st.write("This is a demo deployment for the assignment.")
