from flask import Flask, jsonify
from datetime import datetime, timezone
import random

app = Flask(__name__)

@app.after_request
def add_cors(res):
    res.headers["Access-Control-Allow-Origin"] ="*"
    res.headers["Access-Control-Allow-Methods"] ="GET, OPTIONS"
    res.headers["Access-Control-Allow-Headers"] ="*"
    return res

messages = [
    "Server says hi",
    "Wow, a button click",
    "HTTP 400: this is fine",
    "Ping received, Pong delivered"
]

@app.route("/api",methods=["GET"])
def ping():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d-%H-%M-%S")
    })

@app.route("/message",methods=["GET"])
def message():
    return jsonify({
        "message": random.choice(messages),
    })
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)