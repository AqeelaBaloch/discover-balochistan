
from flask import Flask, render_template, request, jsonify

from data import (
    DESTINATIONS,
    chatbot_reply,
    recommend_destinations,
    build_itinerary
)

import json
import urllib.request
import urllib.error

app = Flask(__name__)


@app.route("/sw.js")
def service_worker():
    response = app.send_static_file("sw.js")
    response.headers["Service-Worker-Allowed"] = "/"
    response.headers["Content-Type"] = "application/javascript"
    return response


# Ollama local AI configuration
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen2.5:1.5b"


@app.route("/")
def home():
    return render_template("index.html", destinations=DESTINATIONS)


@app.route("/api/destinations")
def destinations():
    return jsonify(DESTINATIONS)


# English AI chatbot using Ollama
def ask_local_ai(message):
    tourism_context = json.dumps(
        DESTINATIONS,
        ensure_ascii=False
    )

    system_prompt = f"""
You are Discover Balochistan, an AI-powered tourism assistant.

Your job is to answer questions about tourism in Balochistan.

Use this destination information:
{tourism_context}

Instructions:
1. Always answer in clear and simple English.
2. Give helpful and relevant tourism information.
3. Never invent locations, hotels, prices or contact details.
4. If information is missing, say it is not verified.
5. Do not provide unverified travel safety claims.
6. Keep answers concise and informative.
7. Stay focused on tourism in Balochistan.
"""

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        "stream": False
    }

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=120) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["message"]["content"]


# Chatbot API
@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}

    message = (payload.get("message") or "").strip()
    language = payload.get("language", "en")

    if not message:
        return jsonify({
            "reply": "Please enter a question."
        }), 400

    try:
        if language == "ur":
            reply = chatbot_reply(message, "ur")
        else:
            reply = ask_local_ai(message)

        return jsonify({"reply": reply})

    except (urllib.error.URLError, TimeoutError) as error:
        print("Ollama connection error:", error)

        return jsonify({
            "reply": "The local AI is currently unavailable. Please check whether Ollama is running."
        }), 503

    except Exception as error:
        print("Chatbot error:", error)

        return jsonify({
            "reply": "Sorry, an error occurred while generating your answer."
        }), 500


# Destination recommendation API
@app.route("/api/recommend", methods=["POST"])
def recommend():
    payload = request.get_json(silent=True) or {}

    interests = payload.get("interests", [])

    places = recommend_destinations(interests)

    return jsonify(places)


# Smart Trip Planner API
@app.route("/api/itinerary", methods=["POST"])
def itinerary():
    payload = request.get_json(silent=True) or {}

    destination = payload.get("destination", "")
    days = payload.get("days", 2)
    interests = payload.get("interests", [])
    language = payload.get("language", "en")

    try:
        days = max(1, min(7, int(days)))
    except (TypeError, ValueError):
        days = 2

    if language not in ["en", "ur"]:
        language = "en"

    return jsonify(
        build_itinerary(
            destination,
            days,
            interests,
            language
        )
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
