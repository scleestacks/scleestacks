LABEL org.opencontainers.image.source https://github.com/scleestacks/scleestacks
LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"



# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install pydeseq2
RUN pip install --no-cache-dir pydeseq2==0.4.10

# Test
# >>> from pydeseq2.dds import DeseqDataSet
# >>> from pydeseq2.default_inference import DefaultInference
# >>> from pydeseq2.ds import DeseqStats
# >>> from pydeseq2.utils import load_example_data