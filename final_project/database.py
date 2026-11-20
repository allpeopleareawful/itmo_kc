import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def postgres_connection():
    """Устанавливает и возвращает соединение с PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 6432)),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
    except Exception as e:
        print("❌ Ошибка при подключении к базе данных.")
        raise e

    conn.autocommit = True

    return conn
