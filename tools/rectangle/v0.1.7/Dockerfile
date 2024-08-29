
# Start from a clean Python image
FROM python:3.10-slim

LABEL org.opencontainers.image.source https://github.com/scleestacks/scleestacks
LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"

# Set the working directory in the container
WORKDIR /app

# Install rectangle
RUN pip install --no-cache-dir rectanglepy==0.1.7

# Test
# >>> import rectanglepy as rectangle
# >>> sc_counts, annotations, bulks  = rectangle.load_tutorial_data()