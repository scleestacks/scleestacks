# Stage for scanpy
FROM ghcr.io/scleestacks/scanpy:1.10.2 AS scanpy
RUN pip freeze > /scanpy_reqs.txt

# Stage for scirpy
FROM ghcr.io/scleestacks/scirpy:0.17.2 AS scirpy
RUN pip freeze > /scirpy_reqs.txt

# Stage for muon
FROM ghcr.io/scleestacks/muon:0.1.6 AS muon
RUN pip freeze > /muon_reqs.txt

# Final stage
FROM python:3.10-slim AS final

# Auto-generated labels
LABEL org.opencontainers.image.source="https://github.com/scleestacks/scleestacks" \
      maintainer="Chris Tastad <christopher.tastad@mssm.edu>" \
      org.opencontainers.image.stack_name="airr-multi" \
      org.opencontainers.image.version="1.0.0" \
      org.scleestacks.scanpy.version="1.10.2" \
      org.scleestacks.scirpy.version="0.17.2" \
      org.scleestacks.muon.version="0.1.6"

# Copy requirements files
COPY --from=scanpy /scanpy_reqs.txt /tmp/scanpy_reqs.txt
COPY --from=scirpy /scirpy_reqs.txt /tmp/scirpy_reqs.txt
COPY --from=muon /muon_reqs.txt /tmp/muon_reqs.txt

RUN pip install pip-tools && \
    cat /tmp/scirpy_reqs.txt \
        /tmp/muon_reqs.txt \
        /tmp/scanpy_reqs.txt \
        > /tmp/combined_reqs.txt && \
    pip-compile /tmp/combined_reqs.txt --output-file /tmp/requirements.txt && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/*.txt && \
    rm -rf /root/.cache/pip-tools /root/.cache/pip
