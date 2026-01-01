import chromadb
from chromadb.config import Settings

class VectorStore:
    def __init__(self, collection_name="rag_v21"):
        self.client = chromadb.Client(
            Settings(anonymized_telemetry=False)
        )
        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add(self, embeddings, metadatas, documents):
        self.collection.add(
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents,
            ids=[str(i) for i in range(len(documents))]
        )

    def query(self, query_embedding, top_k=5):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
