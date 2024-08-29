LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"



# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install spatialdata
RUN pip install --no-cache-dir "spatialdata[extra]"==0.2.1

# Test
# >>> from spatialdata.datasets import blobs
# >>> from spatialdata import rasterize, to_circles, to_polygons
# >>> import spatialdata_plot

# https://spatialdata.scverse.org/en/latest/installation.html