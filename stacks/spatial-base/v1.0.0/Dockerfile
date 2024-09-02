# Stage for scanpy
FROM ghcr.io/scleestacks/scanpy:1.10.2 AS scanpy
RUN pip freeze > /scanpy_reqs.txt

# Stage for squidpy
FROM ghcr.io/scleestacks/squidpy:1.6.0 AS squidpy
RUN pip freeze > /squidpy_reqs.txt

# Stage for spatialdata
FROM ghcr.io/scleestacks/spatialdata:0.2.1 AS spatialdata
RUN pip freeze > /spatialdata_reqs.txt

# Final stage
FROM python:3.10-slim AS final

# Auto-generated labels
LABEL org.opencontainers.image.source="https://github.com/scleestacks/scleestacks" \
      maintainer="Chris Tastad <christopher.tastad@mssm.edu>" \
      org.opencontainers.image.stack_name="spatial-base" \
      org.opencontainers.image.version="1.0.0" \
      org.scleestacks.scanpy.version="1.10.2" \
      org.scleestacks.squidpy.version="1.6.0" \
      org.scleestacks.spatialdata.version="0.2.1"

# Copy requirements files
COPY --from=scanpy /scanpy_reqs.txt /tmp/scanpy_reqs.txt
COPY --from=squidpy /squidpy_reqs.txt /tmp/squidpy_reqs.txt
COPY --from=spatialdata /spatialdata_reqs.txt /tmp/spatialdata_reqs.txt

RUN pip install pip-tools && \
    cat /tmp/squidpy_reqs.txt \
        /tmp/spatialdata_reqs.txt \
        /tmp/scanpy_reqs.txt \
        > /tmp/combined_reqs.txt && \
    grep -v "spatialdata==0.2.2" /tmp/combined_reqs.txt | sort -u > /tmp/sorted_reqs.txt && \
    pip-compile /tmp/sorted_reqs.txt --output-file /tmp/requirements.txt && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/*.txt && \
    rm -rf /root/.cache/pip-tools /root/.cache/pip
