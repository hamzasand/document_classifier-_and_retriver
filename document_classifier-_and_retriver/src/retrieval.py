from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


def build_index(documents):

    texts = [doc["text"] for doc in documents]

    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index, embeddings


def search(query, index, documents):

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k=1)

    results = []

    for idx in indices[0]:
        results.append(documents[idx]["filename"])

    return results