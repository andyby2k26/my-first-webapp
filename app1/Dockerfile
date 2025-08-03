# Dockerfile for the first Flask application.
# It builds a Python environment, installs dependencies, and runs the Flask app with Gunicorn.
FROM python:3.11-alpine

WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY . .

# Command to run the Flask application using Gunicorn
# Gunicorn serves the 'app' object from 'app.py' on port 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--forwarded-allow-ips", "*"]