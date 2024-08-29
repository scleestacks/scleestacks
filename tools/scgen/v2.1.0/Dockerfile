
# Start from a clean Python image
FROM python:3.10-slim

LABEL org.opencontainers.image.source https://github.com/scleestacks/scleestacks
LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"

# Set the working directory in the container
WORKDIR /app

RUN apt update && apt install -y pipx git

# Install scgen
RUN pip install --no-cache-dir git+https://github.com/theislab/scgen.git