# Dockerfile for the first Flask application.
# It builds a Python environment, installs dependencies, and runs the Flask app with Gunicorn.
FROM python:3.9-slim-buster

WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY app.py .

# Command to run the Flask application using Gunicorn
# Gunicorn serves the 'app' object from 'app.py' on port 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--forwarded-allow-ips", "*"]