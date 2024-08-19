import chainlit as cl
import zipfile
import os
from file_processing import process_repository
from qa_chain import qa_bot

async def start():
    actions = [
        cl.Action(name="process_repo", value="process", description="Process Repository")
    ]
    await cl.Message(content="Welcome! Click the button to process a repository:", actions=actions).send()

async def on_action(action):
    # Wait for the user to upload a zip file containing the repository
    files = await cl.AskFileMessage(
        content="Please upload a zip file containing the repository to begin!",
        accept=["application/zip"],
        max_files=1,
        max_size_mb=4000  # Adjust the max size based on your needs
    ).send()

    if files:
        zip_file = files[0]
        repo_path = extract_zip(zip_file.path)

        await process_repository(repo_path)
        # Clean up extracted files if necessary
        os.remove(zip_file.path)
    else:
        await cl.Message(content="No zip file uploaded. Please try again.").send()

def extract_zip(zip_path):
    extract_dir = os.path.join(os.path.dirname(zip_path), "extracted_repo")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    return extract_dir

async def main(message):
    # Call qa_bot to get the chains and memory
    rag_chain, direct_chain, memory = qa_bot()

    # Store the chains and memory in the user session
    cl.user_session.set("rag_chain", rag_chain)
    cl.user_session.set("direct_chain", direct_chain)
    cl.user_session.set("memory", memory)

    if message.content.startswith("path:"):
        repo_path = message.content.split("path:")[1].strip()
        await process_repository(repo_path)
    else:
        rag_chain = cl.user_session.get("rag_chain")
        direct_chain = cl.user_session.get("direct_chain")

        res = await cl.AskActionMessage(
            content="How would you like to process this question?",
            actions=[
                cl.Action(name="use_rag", value="use_rag", label="✅ Use RAG"),
                cl.Action(name="no_rag", value="no_rag", label="❌ Don't use RAG"),
            ]
        ).send()

        use_rag = res.get("value") == "use_rag"
        msg = cl.Message(content="")

        if use_rag:
            response = await rag_chain.arun(
                message.content,
                callbacks=[cl.LangchainCallbackHandler()]
            )
        else:
            response = await direct_chain.arun(
                question=message.content,
                callbacks=[cl.LangchainCallbackHandler()]
            )

        await msg.stream_token(response)
        await msg.send()
