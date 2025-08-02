# app2/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Command to run Gunicorn for App 2
# 'app' is the Flask instance name in app.py
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
