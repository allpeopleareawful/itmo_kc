import psycopg2


def postgres_connection():
    """Устанавливает и возвращает соединение с PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host="***REMOVED***",
            port=6432,
            database="startml",
            user="***REMOVED***",
            password="***REMOVED***",
        )
    except Exception as e:
        print("❌ Ошибка при подключении к базе данных.")
        raise e

    conn.autocommit = True

    return conn
