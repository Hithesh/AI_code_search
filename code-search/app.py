import streamlit as st
import json
import numpy as np
from sentence_transformers import SentenceTransformer

st.title("AI Code Semantic Search")

# Load model once
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# Load dataset
@st.cache_data
def load_data():
    return json.load(open("data/code_data.json"))

data = load_data()
texts = [x["text"] for x in data]

# Precompute embeddings
@st.cache_resource
def compute_embeddings():
    return [model.encode(t) for t in texts]

embeddings = compute_embeddings()

query = st.text_input("Enter code description:")

if st.button("Search") and query:

    q_emb = model.encode(query)

    scores = [
        np.dot(q_emb, emb)/(np.linalg.norm(q_emb)*np.linalg.norm(emb))
        for emb in embeddings
    ]

    top = sorted(zip(scores, texts), reverse=True)[:5]

    st.subheader(" Results")

    for s,t in top:
        st.write(f"Score: {s:.3f}")
        st.code(t)
