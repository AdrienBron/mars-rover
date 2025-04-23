FROM python:3.13-alpine

WORKDIR /app

RUN apk add --no-cache postgresql-dev gcc musl-dev \
    && pip install psycopg2

COPY server.py .

CMD ["python", "server.py"]
