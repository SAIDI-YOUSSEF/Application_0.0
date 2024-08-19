import os
from concurrent.futures import ThreadPoolExecutor
import chainlit as cl
from config import TEXT_EXTENSIONS
from vectorstore import create_vectorstore
from qa_chain import qa_bot
from config import QDRANT_COLLECTION_NAME

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read() + "\n\n"
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

def process_repo(repo_path):
    text_content = ""
    file_paths = []

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.lower().endswith(TEXT_EXTENSIONS):
                file_paths.append(os.path.join(root, file))

    with ThreadPoolExecutor() as executor:
        results = executor.map(read_file, file_paths)

    for result in results:
        text_content += result

    return text_content

async def process_repository(repo_path):
    msg = cl.Message(content="Processing repository...")
    await msg.send()

    text_content = process_repo(repo_path)
    vectorstore = await create_vectorstore(text_content)

    msg.content = f"Repository processed and vectorstore created in Qdrant collection: {QDRANT_COLLECTION_NAME}"
    await msg.update()

    rag_chain, direct_chain, memory = qa_bot()
    cl.user_session.set("rag_chain", rag_chain)
    cl.user_session.set("direct_chain", direct_chain)
    cl.user_session.set("memory", memory)
