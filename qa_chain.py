from langchain.chains import RetrievalQA, LLMChain
from langchain.memory.buffer import ConversationBufferMemory
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_community.embeddings import OllamaEmbeddings
from config import QDRANT_URL, QDRANT_API_KEY, QDRANT_COLLECTION_NAME
from llm import load_llm
from prompts import set_rag_prompt, set_direct_prompt


def retrieval_qa_chain(llm, prompt, db, memory):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 5}),
        memory=memory,
        chain_type_kwargs={"prompt": prompt}
    )
    return qa_chain

def qa_bot():
    embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    db = QdrantVectorStore(
        client=client,
        collection_name=QDRANT_COLLECTION_NAME,
        embedding=embeddings
    )
    llm = load_llm()
    rag_prompt = set_rag_prompt()
    direct_prompt = set_direct_prompt()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    rag_chain = retrieval_qa_chain(llm, rag_prompt, db, memory)
    direct_chain = LLMChain(llm=llm, prompt=direct_prompt, memory=memory)
    return rag_chain, direct_chain, memory
