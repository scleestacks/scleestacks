
# Start from a clean Python image
FROM python:3.10-slim

LABEL org.opencontainers.image.source https://github.com/scleestacks/scleestacks
LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"

# Set the working directory in the container
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Install scvi-tools
RUN pip install --no-cache-dir scvi-tools==1.1.5

