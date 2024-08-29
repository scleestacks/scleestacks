LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"



# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install squidpy
RUN pip install --no-cache-dir squidpy==1.6.0

# Test
# >>> import squidpy as sq
# >>> adata = sq.datasets.imc()

# https://squidpy.readthedocs.io/en/stable/index.html