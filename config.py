import os
import uuid

# Qdrant configuration
QDRANT_URL = "https://40d100bc-5b08-4a43-81cf-f30f13ee4cca.us-east4-0.gcp.cloud.qdrant.io:6333"
QDRANT_API_KEY = "2OmPRfRryg9SzFmA58lcvp-IPGwBkBB249DPD61TVffVJSYH5tlrIg"
def generate_collection_name():
    return f"repo_{uuid.uuid4().hex[:8]}"

QDRANT_COLLECTION_NAME = generate_collection_name()

# Groq API key
GROQ_API_KEY = "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"

# Supported file extensions
TEXT_EXTENSIONS = ('.txt', '.py', '.js', '.html', '.css', '.md', '.json', '.xml', '.yml', '.yaml', '.ini', '.cfg', '.java')
