# Use Python slim image based on Debian
FROM python:3.9-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Specify the port the app will run on (if applicable)
EXPOSE 8000

# Define the command to run the application
CMD ["python", "app.py"]

