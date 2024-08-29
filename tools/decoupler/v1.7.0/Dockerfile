LABEL org.opencontainers.image.source="https://github.com/scleestacks/scleestacks"
LABEL maintainer="christopher.tastad@mssm.edu"


# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install decoupler
RUN pip install --no-cache-dir decoupler==1.7.0 && \
   pip install --no-cache-dir scipy==1.14.0     && \
   pip install --no-cache-dir anndata==0.10.8   && \
   pip install --no-cache-dir omnipath==1.0.8 
  
# Test
# >>> import decoupler as dc
# >>> net = dc.get_collectri(organism='human', split_complexes=False)
