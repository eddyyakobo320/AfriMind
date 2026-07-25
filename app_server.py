# ==========================================
# AfriMind AI Web Server
# Version 28.2
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from flask import Flask, request, jsonify

from core.ai_engine import ask_question



# ==========================================
# CREATE APP
# ==========================================

app = Flask(__name__)




# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return open(
        "frontend/index.html",
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
        debug=True
    )