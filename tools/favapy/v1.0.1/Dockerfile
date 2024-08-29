LABEL org.opencontainers.image.source="https://github.com/scleestacks/scleestacks"
LABEL maintainer="christopher.tastad@mssm.edu"


# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install favapy
RUN pip install --no-cache-dir favapy==1.0.1

