# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt to install dependencies
COPY requirements.txt .

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire project directory
COPY . .

# Set environment variables (optional, can be overridden in docker-compose.yml or .env)
ENV PYTHONUNBUFFERED=1

# Command to run the scraper
CMD ["python", "scripts/main.py"]