# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install moscot
RUN pip install --no-cache-dir moscot==0.3.4
RUN pip install --no-cache-dir ott-jax==0.4.6

# Test
# >>> import moscot as mt
# >>> import moscot.plotting as mtp
# >>> from moscot.problems.time import LineageProblem, TemporalProblem
