
# Start from a clean Python image
FROM python:3.10-slim

LABEL org.opencontainers.image.source https://github.com/scleestacks/scleestacks
LABEL maintainer="Chris Tastad <christopher.tastad@mssm.edu>"

# Set the working directory in the container
WORKDIR /app

# Install SC2Spa
RUN pip install --no-cache-dir SC2Spa==1.3.0

# Test 1
# >>> import SC2Spa 

# Test 2
# >>> from SC2Spa import tl, pp, pl, sva

# To get Test 2 working, you need to uncomment the following code and run it
# RUN pip install --no-cache-dir numpy==2.0.1 \
#     && pip install --no-cache-dir pandas==2.2.2 \
#     && pip install --no-cache-dir anndata==0.10.8 \
#     && pip install --no-cache-dir scikit-learn==1.5.1 \
#     && pip install --no-cache-dir tensorflow==2.17.0 \
#     && pip install --no-cache-dir ipython==8.26.0 \
#     && pip install --no-cache-dir matplotlib==3.9.1 \
#     && pip install --no-cache-dir seaborn==0.13.2

