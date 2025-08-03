# app2/Dockerfile
# Dockerfile for the second Flask application.
# Identical to app1's Dockerfile, as the setup is the same.
FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--forwarded-allow-ips", "*"]