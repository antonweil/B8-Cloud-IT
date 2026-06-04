from flask import Flask, jsonify
from datetime import datetime, timezone
import requests

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    # ping owns status + timestamp, and delegates the message to the message service.
    # (To fully decouple, give ping its own message list instead of this call.)
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d-%H-%M-%S"),
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
