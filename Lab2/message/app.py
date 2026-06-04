from flask import Flask, jsonify
import random

app = Flask(__name__)

messages = [
    "Server says hi",
    "Wow, a button click",
    "HTTP 400: this is fine",
    "Ping received, Pong delivered",
    "Like many things in this museum, this Server is DEAD"
]

@app.route("/message", methods=["GET"])
def message():
    return jsonify({"message": random.choice(messages)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
