# Start from a clean Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install scanpro
RUN pip install --no-cache-dir scanpro==0.3.2

# Test
# >>> from scanpro import scanpro
# >>> from scanpro import scanpro, anova, t_test
# >>> from scanpro.linear_model import create_design
# >>> from scanpro.get_transformed_props import get_transformed_props