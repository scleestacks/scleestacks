LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"



# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install scalex
RUN pip install --no-cache-dir scalex==1.0.4

# Test
# >>> import scalex
# >>> from scalex.function import SCALEX
# >>> from scalex.plot import embedding