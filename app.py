import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = Flask(__name__)

SYSTEM_PROMPT = """
You are CareGuide, an educational medical information assistant. Be empathetic, concise,
and clear. You are not a doctor and must not diagnose, prescribe, or claim certainty.
Ask clarifying questions when useful. Offer general information and encourage users to
consult a licensed healthcare professional for personal medical decisions.
If the user describes possible emergency symptoms (such as severe trouble breathing,
chest pain, signs of stroke, severe bleeding, loss of consciousness, or immediate danger),
tell them to contact local emergency services now and not wait for a chatbot response.
Do not ask for or encourage sharing full names, phone numbers, addresses, or other
identifying details. Never imply that chat messages are confidential medical records.
For medication questions, do not recommend starting/stopping prescription medication.
"""
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/status")
def status():
    return jsonify({"configured": client is not None})

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    messages = data.get("messages", [])
    if not isinstance(messages, list) or not messages:
        return jsonify({"error": "Please enter a message."}), 400
    # Keep the request small and accept only user/assistant text messages.
    cleaned = []
    for msg in messages[-12:]:
        if not isinstance(msg, dict) or msg.get("role") not in ("user", "assistant"):
            continue
        content = msg.get("content")
        if isinstance(content, str) and content.strip():
            cleaned.append({"role": msg["role"], "content": content[:5000]})
    if not cleaned or cleaned[-1]["role"] != "user":
        return jsonify({"error": "Please send a user message."}), 400
    if client is None:
        return jsonify({"error": "The API is not configured yet. Add your OpenAI API key to the .env file, then restart the server."}), 503
    try:
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            messages=[{"role": "system", "content": SYSTEM_PROMPT}, *cleaned],
            temperature=0.4,
        )
        answer = response.choices[0].message.content or "Sorry, I couldn't generate a response."
        return jsonify({"reply": answer})
    except Exception:
        app.logger.exception("OpenAI request failed")
        return jsonify({"error": "The AI service request failed. Check your API key, billing, and network, then try again."}), 502

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "false").lower() == "true")
