#!/bin/bash

# Define your Docker registry and image name
DOCKER_REGISTRY="0kanh0llander"
IMAGE_NAME="rollingupdatewebapp"
IMAGE_TAG="v1"

# Build the Docker image from the current directory
docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .

# Authenticate with your Docker registry (if needed)
# docker login "${DOCKER_REGISTRY}"

# Tag the image for the registry
docker tag "${IMAGE_NAME}:${IMAGE_TAG}" "${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"

# Push the image to the Docker registry
docker push "${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"

# Optionally, log out from the Docker registry (if you logged in earlier)
# docker logout "${DOCKER_REGISTRY}"

echo "Docker image '${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}' has been built and pushed to the registry."
