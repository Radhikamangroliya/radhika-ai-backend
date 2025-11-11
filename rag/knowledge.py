import chromadb

# ✅ New Chroma client (persistent)
chroma_client = chromadb.PersistentClient(path="rag_db")

# ✅ Create / load knowledge collection
collection = chroma_client.get_or_create_collection(
    name="radhika_knowledge",
    metadata={"hnsw:space": "cosine"}
)
