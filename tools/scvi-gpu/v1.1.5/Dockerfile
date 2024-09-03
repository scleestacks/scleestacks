# Base image
FROM nvidia/cuda:12.1.0-devel-ubuntu22.04

LABEL org.opencontainers.image.source https://github.com/scleestacks/scleestacks
LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"

# Install required system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.10 \
    python3-pip \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a symbolic link for python3.10
RUN ln -s /usr/bin/python3.10 /usr/local/bin/python3 && \
    ln -s /usr/bin/pip3 /usr/local/bin/pip

RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
    torch \
    torchvision \
    torchaudio \
    --index-url https://download.pytorch.org/whl/cu121 && \
    pip install --no-cache-dir jax[cuda12] -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
    pip install --no-cache-dir scvi-tools==1.1.5 && \
    rm -rf /root/.cache/pip

