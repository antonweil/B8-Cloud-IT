from flask import Flask, Response
import requests

app = Flask(__name__)

# Map public paths -> internal service URLs.
# Service names ("ping", "message") resolve via Docker's internal DNS on app-net.
ROUTES = {
    "/api":     "http://ping:8000/ping",
    "/message": "http://message:8000/message",
}

@app.after_request
def add_cors(res):
    # CORS lives ONLY here, because the gateway is the only service the browser hits.
    res.headers["Access-Control-Allow-Origin"]  = "*"
    res.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    res.headers["Access-Control-Allow-Headers"] = "*"
    return res

def proxy(target):
    try:
        r = requests.get(target, timeout=5)
    except requests.RequestException as e:
        return Response('{"error":"upstream unreachable"}',
                        status=502, content_type="application/json")
    return Response(r.content, status=r.status_code,
                    content_type=r.headers.get("content-type", "application/json"))

@app.route("/api", methods=["GET"])
def api():
    return proxy(ROUTES["/api"])

@app.route("/message", methods=["GET"])
def message():
    return proxy(ROUTES["/message"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
