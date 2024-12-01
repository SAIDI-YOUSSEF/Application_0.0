import os
import uuid

# Qdrant configuration
QDRANT_URL = ""
QDRANT_API_KEY = ""
def generate_collection_name():
    return f"repo_{uuid.uuid4().hex[:8]}"

QDRANT_COLLECTION_NAME = generate_collection_name()

# Groq API key
GROQ_API_KEY = ""

# Supported file extensions
TEXT_EXTENSIONS = ('.txt', '.py', '.js', '.html', '.css', '.md', '.json', '.xml', '.yml', '.yaml', '.ini', '.cfg', '.java')
