# document-qa-bot-rag
A Retrieval-Augmented Generation (RAG) based Document Q&amp;A Bot that extracts text from PDF documents, generates Gemini embeddings, stores vectors in ChromaDB, and answers user questions using semantic search and Gemini AI.
# Document Q&A Bot using RAG

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline for answering questions from uploaded documents.

## Features

* PDF document ingestion
* Text extraction using PyPDF
* Text chunking with overlap
* Embedding generation using Gemini Embedding Model
* Vector storage using ChromaDB
* Semantic search
* Question answering using Gemini

## Tech Stack

* Python
* Google Gemini
* ChromaDB
* PyPDF
* Google Colab

## Workflow

Document Upload → Text Extraction → Chunking → Embeddings → ChromaDB → Retrieval → Gemini Answer Generation

## Example

Question:
"What are the common mistakes that reduce IELTS Writing scores?"

Answer:
The system retrieves relevant document chunks and generates a grounded response using Gemini.

## Future Improvements

* Streamlit UI
* Citation support
* Multiple document support
* Persistent vector database
