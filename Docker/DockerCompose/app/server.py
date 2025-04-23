import os
import psycopg2
import time

host = os.getenv("DB_HOST", "localhost")
dbname = os.getenv("DB_NAME", "mydb")
user = os.getenv("DB_USER", "postgres")
password = os.getenv("DB_PASS", "")

print("📡 Tentative de connexion à la base de données...")

for _ in range(10):
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        print("✅ Connexion réussie ! user:", user, "host:", host, "dbname:", dbname, "password:", password)
        conn.close()
        break
    except Exception as e:
        print("❌ Connexion échouée, nouvelle tentative...")
        print(e)
        time.sleep(2)
