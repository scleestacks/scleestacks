LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"



# Start from a clean Python image, incompatible with python >= 3.10
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

RUN pip install --no-cache-dir FlowSom==0.1.1

# RUN apt update && apt install -y pipx git

# # Install flowsom
# RUN pip install --no-cache-dir git+https://github.com/saeyslab/FlowSOM_Python

