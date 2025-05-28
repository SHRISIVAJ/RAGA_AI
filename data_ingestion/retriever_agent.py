import faiss
import numpy as np

class RetrieverAgent:
    def __init__(self):
        self.index = faiss.IndexFlatL2(128)  # Example size of the embedding vector

    def index_data(self, embeddings):
        self.index.add(np.array(embeddings))

    def retrieve(self, query_embedding, k=5):
        _, indices = self.index.search(np.array([query_embedding]), k)
        return indices
