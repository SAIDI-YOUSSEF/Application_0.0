import chainlit as cl
from config import QDRANT_COLLECTION_NAME
from ui import start, on_action, main
from file_processing import process_repository
from qa_chain import qa_bot

@cl.on_chat_start
async def start_chat():
    await start()

@cl.action_callback("process_repo")
async def process_repo_action(action):
    await on_action(action)

@cl.on_message
async def handle_message(message):
    await main(message)

if __name__ == "__main__":
    cl.run()
