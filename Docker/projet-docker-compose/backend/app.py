from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"ping": "pong"})

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
        )
        conn.close()
        return jsonify({"status": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

app.run(host="0.0.0.0", port=5000)
