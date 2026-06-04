#!/usr/bin/env bash
set -euo pipefail

# Forward gateway (API) and frontend (UI) to localhost in one go.
# Ctrl-C stops BOTH cleanly. Keep this terminal open while you use the app.

# Kill both background forwards when this script exits for any reason.
cleanup() { kill 0 2>/dev/null; }
trap cleanup EXIT INT TERM

echo "Waiting for pods to be ready..."
kubectl wait --for=condition=ready pod -l app=gateway  --timeout=120s
kubectl wait --for=condition=ready pod -l app=frontend --timeout=120s

echo
echo "Forwarding:"
echo "  API  -> http://127.0.0.1:8000   (svc/gateway)"
echo "  UI   -> http://127.0.0.1:3000   (svc/frontend)"
echo "Open http://127.0.0.1:3000 in your browser. Ctrl-C to stop."
echo

kubectl port-forward svc/gateway  8000:8000 &
kubectl port-forward svc/frontend 3000:80   &

wait   # block here until Ctrl-C, then trap fires and kills both
