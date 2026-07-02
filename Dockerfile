# Base Image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run application
CMD ["python", "app.py"]