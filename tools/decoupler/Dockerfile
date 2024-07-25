# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install decoupler
RUN pip install --no-cache-dir decoupler && \
    pip install --no-cache-dir scipy     && \
    pip install --no-cache-dir anndata   && \
    pip install --no-cache-dir omnipath  
    
# Test
# >>> import decoupler as dc
# >>> net = dc.get_collectri(organism='human', split_complexes=False)