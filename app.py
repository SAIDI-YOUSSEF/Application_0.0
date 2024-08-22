import chainlit as cl
from config import QDRANT_COLLECTION_NAME
from ui import start, on_action, main
from file_processing import process_repository
from qa_chain import qa_bot
from chainlit.server import app 


@cl.on_chat_start
async def start_chat():
    await start()

@cl.action_callback("process_repo")
async def process_repo_action(action):
    try:
        await on_action(action)  # Call the action handler
        # Process the repository asynchronously
        await process_repository(action)  # Ensure this is an async call
    except Exception as e:
        await cl.Message(content=f"An error occurred: {e}").send()

@cl.on_message
async def handle_message(message):
    await main(message)

if __name__ == "__app__":
    cl.run()
    
    