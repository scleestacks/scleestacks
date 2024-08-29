LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"



# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

RUN apt update && apt install -y pipx git

# Install cell2location (commit b2f3894), the lastest version 0.1.3 is not working
RUN pip install --no-cache-dir git+https://github.com/BayraktarLab/cell2location.git

# Install cell2location (instruction on their github, not working)
# RUN pip install --no-cache-dir cell2location[tutorials]
# RUN pip install torch torchvision torchaudio

# # Install cell2location v0.1.3 
# RUN pip install --no-cache-dir cell2location==0.1.3 
# RUN pip install --no-cache-dir scvi-tools==1.0.4
# RUN pip install --no-cache-dir jaxlib==0.4.23
# RUN pip install --no-cache-dir jax==0.4.23
# RUN pip install --no-cache-dir scipy==1.11.3

