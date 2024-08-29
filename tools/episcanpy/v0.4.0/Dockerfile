LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"



# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install episcanpy
RUN pip install --no-cache-dir episcanpy==0.4.0

# Test 
# >>> import episcanpy.api as epi (on the tutorial, doesn't work)
# >>> import episcanpy as epi (when import episcanpy, should use this instead)