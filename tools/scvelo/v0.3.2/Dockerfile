LABEL org.opencontainers.image.source https://github.com/scleestacks/scleestacks
LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"



# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the contain
WORKDIR /app

# Install scvelo
RUN pip install --no-cache-dir -U scvelo==v0.3.2

# >>> import scvelo as scv
# >>> scv.set_figure_params()
# >>> scv.datasets.pancreas()

# https://github.com/theislab/scvelo