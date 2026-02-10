from sentence_transformers import SentenceTransformer
import numpy as np
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

data = json.load(open("data/code_data.json"))

texts = [x["text"] for x in data]

print("Generating embeddings...")
embeddings = [model.encode(t) for t in texts]


def search(query):

    q_emb = model.encode(query)

    scores = [
        np.dot(q_emb, emb)/(np.linalg.norm(q_emb)*np.linalg.norm(emb))
        for emb in embeddings
    ]

    top = sorted(zip(scores, texts), reverse=True)[:5]

    print("\n Results:\n")

    for s,t in top:
        print(f"Score: {s:.3f}")
        print(t)
        print("-"*50)


while True:
    q = input("Search query: ")
    search(q)
