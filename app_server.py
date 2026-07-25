from flask import Flask, request, jsonify
from core.ai_engine import ask_question

app = Flask(__name__)


@app.route("/")
def home():
    return open("frontend/index.html").read()


@app.route("/ask", methods=["POST"])
def ask():

    data = request.json

    question = data["question"]

    answer = ask_question(question)

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":
    app.run(debug=True)