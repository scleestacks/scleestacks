# Stage for scanpy
FROM ghcr.io/scleestacks/scanpy:1.10.2 AS scanpy
RUN pip freeze > /scanpy_reqs.txt

# Stage for scvi
FROM ghcr.io/scleestacks/scvi-gpu:1.1.5 AS scvi
RUN pip freeze > /scvi_reqs.txt

# Final stage
FROM nvidia/cuda:12.1.0-devel-ubuntu22.04 AS final

# Auto-generated labels
LABEL org.opencontainers.image.source="https://github.com/scleestacks/scleestacks" \
      maintainer="Chris Tastad <christopher.tastad@mssm.edu>" \
      org.opencontainers.image.stack_name="scvi-gpu-base" \
      org.opencontainers.image.version="1.0.0" \
      org.scleestacks.scanpy.version="1.10.2"

# Copy requirements files
COPY --from=scanpy /scanpy_reqs.txt /tmp/scanpy_reqs.txt
COPY --from=scvi /scvi_reqs.txt /tmp/scvi_reqs.txt

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

RUN pip install pip-tools && \
    cat /tmp/scanpy_reqs.txt \
        /tmp/scvi_reqs.txt \
        > /tmp/combined_reqs.txt && \
    grep -v "networkx==3.2.1" /tmp/combined_reqs.txt | \
    grep -v "numpy==1.26.3" | \
    grep -v "pillow==10.2.0" | \
    sort -u > /tmp/sorted_reqs.txt

RUN pip-compile \
    --extra-index-url https://download.pytorch.org/whl/cu121 \
    /tmp/sorted_reqs.txt \
    --output-file /tmp/requirements.txt

RUN pip install --no-cache-dir \
    --extra-index-url https://download.pytorch.org/whl/cu121 \
    -r /tmp/requirements.txt && \
    rm /tmp/*.txt && \
    rm -rf /root/.cache/pip-tools /root/.cache/pip

