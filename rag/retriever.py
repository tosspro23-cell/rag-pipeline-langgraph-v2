def retrieve(query, embedder, store, top_k=5):
    query_embedding = embedder.embed([query])[0]
    results = store.query(query_embedding, top_k=top_k)
    return results
