from langchain.prompts import PromptTemplate

rag_prompt_template = """You are a highly advanced code assistant designed to assist developers in understanding, 
modifying, and improving their web applications. 
You have access to a comprehensive codebase consisting of multiple files. 
Your primary function is to provide informative and helpful responses to developer inquiries about the code.
Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

direct_prompt_template = """You are a highly advanced code assistant designed to assist developers with their coding queries.
Your primary function is to provide informative and helpful responses to developer inquiries about coding.

Question: {question}

Provide a helpful and informative answer:
"""

def set_rag_prompt():
    return PromptTemplate(template=rag_prompt_template, input_variables=["context", "question"])

def set_direct_prompt():
    return PromptTemplate(template=direct_prompt_template, input_variables=["question"])
