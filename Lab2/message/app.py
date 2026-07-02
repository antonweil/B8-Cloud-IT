from flask import Flask, jsonify
import random, json, os
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

conn      = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
container = os.environ.get("MESSAGES_CONTAINER", "container")
blob_name = os.environ.get("MESSAGES_BLOB", "messages.json")

blob_service = BlobServiceClient.from_connection_string(conn)

def load_messages():
    blob = blob_service.get_blob_client(container=container, blob=blob_name)
    data = blob.download_blob().readall()   # bytes
    return json.loads(data)

messages = load_messages()

@app.route("/message", methods=["GET"])
def message():
    return jsonify({"message": random.choice(list(messages.values()))})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
