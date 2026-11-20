from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import random


def get_top_liker():
    postgres = PostgresHook(postgres_conn_id='startml_feed')
    with postgres.get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
            SELECT user_id, COUNT(*) as likes_count
            FROM feed_action
            WHERE action = 'like'
            GROUP BY user_id
            ORDER BY likes_count DESC
            LIMIT 1
        ''')
            result = cursor.fetchone()

    if result:
        user_id, count = result

        return {"user_id": user_id, "count": count}
    
    return None

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="hw_11_egor-kozlov-bjc-3489",
    start_date=datetime(2022, 1, 1),
    schedule=timedelta(days=1),
    default_args=default_args,
    catchup=False,
    tags=["example"],
) as dag:
    get_top = PythonOperator(
        task_id="get_top_liker",
        python_callable=get_top_liker,
    )

    get_top
