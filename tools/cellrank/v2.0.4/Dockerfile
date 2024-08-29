LABEL org.opencontainers.image.source https://github.com/scleestacks/scleestacks
LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"



# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install cellrank
RUN pip install --no-cache-dir cellrank==2.0.4

# Test
# >>> import cellrank as cr
# >>> adata = cr.datasets.bone_marrow()
