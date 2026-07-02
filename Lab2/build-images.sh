#!/usr/bin/env bash
set -euo pipefail

# Build all four images straight into minikube's OWN Docker daemon, so the
# cluster can use them with no registry. Without this, kubectl would try to
# pull "gateway:local" from Docker Hub and fail with ErrImagePull.
#
# Run from anywhere; this cds to the project root automatically.
cd "$(dirname "$0")"

eval "$(minikube docker-env)"   # point `docker` at minikube's daemon (this shell only)

docker build -t gateway:local  ./gateway
docker build -t ping:local     ./ping
docker build -t message:local  ./message
docker build -t frontend:local ./frontend

echo
echo "Done. Verify with:  minikube image ls | grep ':local'"
