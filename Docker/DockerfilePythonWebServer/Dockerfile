# Dockerfile 3 - Python web server
FROM python:3.13-alpine

WORKDIR /app

# Installer curl et pip de base + mise à jour setuptools
RUN apk add --no-cache curl && \
    pip install --upgrade pip setuptools

COPY server.py .

EXPOSE 8000

CMD ["python", "server.py"]

