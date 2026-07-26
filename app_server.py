# ==========================================
# AfriMind AI Web Server
# Version 28.3
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================

from flask import Flask, request, jsonify
from core.ai_engine import ask_question

import os


# ==========================================
# CREATE APP
# ==========================================

app = Flask(__name__)


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    file_path = os.path.join(
        "Frontend",
        "index.html"
    )

    return open(
        file_path,
        encoding="utf-8"
    ).read()



# ==========================================
# ASK AFRIMIND
# ==========================================

@app.route("/ask", methods=["POST"])
def ask():

    data = request.json

    question = data.get(
        "question",
        ""
    )

    answer = ask_question(
        question
    )

    return jsonify({

        "answer": answer

    })



# ==========================================
# START SERVER
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )