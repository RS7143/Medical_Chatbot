# CareGuide Medical Assistant Website

A responsive medical-information chatbot website based on the uploaded command-line assistant concept. It replaces terminal prompts and local audio/PDF workflow with a browser chat interface and OpenAI-powered responses.

## Run on Windows (VS Code)

1. Install Python 3.10 or newer.
2. Extract this folder and open it in VS Code.
3. Open the VS Code terminal in this folder.
4. Create a virtual environment (recommended):

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

5. Install packages:

   ```powershell
   pip install -r requirements.txt
   ```

6. Copy `.env.example` to a new file named `.env`.
7. Open `.env` and replace the placeholder with your own API key from the OpenAI platform. Keep the key private; never put it in `static/app.js`, HTML, or a public repository.
8. Start the server:

   ```powershell
   python app.py
   ```

9. Open http://127.0.0.1:5000 in your browser.


