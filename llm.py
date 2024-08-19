from langchain_groq.chat_models import ChatGroq
from config import GROQ_API_KEY

def load_llm():
    return ChatGroq(
        temperature=0.5,
        model="llama3-70b-8192",
        api_key=GROQ_API_KEY,
    )
