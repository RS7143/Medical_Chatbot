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

## Important

- No real API key is included. API calls are made by the Python server so the key is not exposed to browser JavaScript.
- API usage may incur charges depending on your account and model access.
- The assistant provides general information only; it does not diagnose conditions or replace a clinician.
- Do not collect or store patient names, phone numbers, or medical records in this demo. Chat history stays in the current browser page and is not saved to a database by this app.
- For a public deployment, use HTTPS, add authentication and rate limiting, configure secure hosting, and get appropriate privacy/security review before handling health information.
- This demo does not implement the original code's voice input/output, symptom JSON matching, PDF export, or MongoDB storage. Those should be added deliberately with secure handling and testing if required.
