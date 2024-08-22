
# Code-Assist
The Chainlit Code Assistant is a powerful chatbot application designed to help you with code-related tasks. With this app, you can upload an entire code repository or an entire application and engage in detailed discussions about your code. The chatbot provides assistance with code understanding, debugging, and other coding functionalities, making it a valuable tool for developers seeking help with their projects.




## Prerequisites


Before running the application, ensure you have the following installed on your system:

- **Python 3.8+**: The application requires Python 3.8 or later. Follow these steps to install Python:

  ### Installing Python

  - **On Windows**:
    1. Download the Python installer from the [official Python website](https://www.python.org/downloads/).
    2. Run the installer and select the option to "Add Python to PATH."
    3. Click "Install Now" and follow the prompts to complete the installation.

  - **On macOS**:
    1. You can install Python using Homebrew. If Homebrew is not installed, first install it by following instructions at [brew.sh](https://brew.sh/).
    2. Open Terminal and run:
       ```bash
       brew install python
       ```

  - **On Linux**:
    1. Use your package manager to install Python. For example, on Debian-based systems (like Ubuntu), you can run:
       ```bash
       sudo apt update
       sudo apt install python3
       ```

.


## Setup



### Local Setup

1. **Clone the Repository**


2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Get the Embedder**

   To get the embedder locally, run the following command:

   ```bash
   ollama pull nomic-embed-text
   ```

5. **Configuration**

   Ensure you have the necessary configuration files. Create a `config.py` file in the root directory with the required configuration settings. Obtain the API keys from the following links:

   - **Qdrant API Key**: [Qdrant Authentication](https://qdrant.tech/documentation/cloud/authentication/)
   - **Groq API Key**: [Groq Console](https://console.groq.com/keys)

   Example `config.py` file:

   ```python
   QDRANT_URL = "http://localhost:6333"
   QDRANT_API_KEY = "your_qdrant_api_key"
   GROQ_API_KEY = "your_groq_api_key"
   ```

6. **Run the Application**

   ```bash
   chainlit run app.py
   ```

   Replace `app.py` with the entry point of your Chainlit application if it's different.

---

## Usage

Access the App: Open your web browser and go to http://localhost:8000 (or the appropriate port if different).

Interaction: Follow the on-screen instructions to interact with the application.
## Troubleshooting

## Troubleshooting

- **Common Issues**:
  - If the app crashes or exhibits unexpected behavior, check the logs for error messages.
  - Verify that all environment variables are correctly set up in `config.py`.

- **Debugging**:
  - To gather more information and troubleshoot issues, you can run the app in debug mode with the following command:

    ```bash
    chainlit run app.py -d
    ```

  - Running the app in debug mode provides more detailed logs that can help identify the source of the problem.

---

