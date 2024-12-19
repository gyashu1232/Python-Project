# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .  # Copy all files including 'tests'

CMD ["python", "app.py"]
