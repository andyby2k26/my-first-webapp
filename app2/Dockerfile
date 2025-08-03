FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache \
    build-base \
    python3-dev \
    postgresql-dev

# Install dependencies
RUN apk add --no-cache postgresql-dev gcc musl-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--forwarded-allow-ips", "*"]
