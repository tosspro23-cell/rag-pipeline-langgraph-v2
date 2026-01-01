from rag.loader import load_documents
from rag.chunker import chunk_documents
from rag.embedder import Embedder
from rag.vectorstore import VectorStore
from rag.retriever import retrieve
from eval.debug import print_results

DATA_DIR = "data/documents"

def main():
    query = input("Enter your query: ")

    print("Loading documents...")
    docs = load_documents(DATA_DIR)

    print("Chunking...")
    chunks = chunk_documents(docs)

    print(f"Total chunks: {len(chunks)}")

    embedder = Embedder()
    store = VectorStore()

    print("Embedding & indexing...")
    embeddings = embedder.embed([c["text"] for c in chunks])

    store.add(
        embeddings=embeddings,
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"]} for c in chunks]
    )

    print("Retrieving...")
    results = retrieve(query, embedder, store)

    print_results(results)

if __name__ == "__main__":
    main()
