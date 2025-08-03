# app2/Dockerfile
# Dockerfile for the second Flask application.
# Identical to app1's Dockerfile, as the setup is the same.
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--forwarded-allow-ips", "*"]