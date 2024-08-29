LABEL org.opencontainers.image.source="https://github.com/scleestacks/scleestacks"
LABEL maintainer="christopher.tastad@mssm.edu"


# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install hotspotsc
RUN pip install --no-cache-dir hotspotsc==1.1.1

