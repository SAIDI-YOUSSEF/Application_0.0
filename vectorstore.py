import chainlit as cl
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from config import QDRANT_URL, QDRANT_API_KEY, QDRANT_COLLECTION_NAME

async def create_vectorstore(text_content):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=0)
    texts = text_splitter.split_text(text_content)
    embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
    
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    client.create_collection(
        collection_name=QDRANT_COLLECTION_NAME,
        vectors_config=VectorParams(size=768, distance=Distance.COSINE),
    )
    vectorstore = QdrantVectorStore(
        client=client,
        collection_name=QDRANT_COLLECTION_NAME,
        embedding=embeddings,
    )

    batch_size = 5
    total_chunks = len(texts) + 1
    progress = 0
    progress_increment = 100 / total_chunks

    for i in range(0, total_chunks, batch_size):
        batch_texts = texts[i:i + batch_size]
        vectorstore.add_texts(batch_texts)
        progress += progress_increment * len(batch_texts)
        await cl.Message(content=f"Processing: {int(progress)}% complete").send()

    return vectorstore
