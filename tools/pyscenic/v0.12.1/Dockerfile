LABEL org.opencontainers.image.source="https://github.com/scleestacks/scleestacks"
LABEL maintainer="christopher.tastad@mssm.edu"


# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install pyscenic
RUN pip install --no-cache-dir pyscenic==0.12.1
# Install numpy (The installed numpy version, NumPy 1.20, is not compatible)
RUN pip install --no-cache-dir numpy==1.23.5

# Test
# >>> from pyscenic.prune import prune2df, df2regulons
