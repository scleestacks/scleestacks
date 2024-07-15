# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
# WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
# COPY . .

# Set the PIP default timeout to 3000 seconds
# ENV PIP_DEFAULT_TIMEOUT=3000

# Upgrade pip
RUN pip install --upgrade pip

# Install scvi-tools
RUN pip install --no-cache-dir scvi-tools 

# Make port 8888 available to the world outside this container
# EXPOSE 8888

# Define environment variable
# ENV NAME scvi-tools

# Run a Jupyter notebook server when the container launches
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]


