from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random


def fetch_data(ti):
    ti.xcom_push(key="sample_xcom_key", value='xcom test')


def analyze_data(ti):
    results = ti.xcom_pull(key="sample_xcom_key", task_ids="fetch_data")
    print(results)

    


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="xcom_test",
    start_date=datetime(2022, 1, 1),
    schedule=timedelta(days=1),
    default_args=default_args,
    catchup=False,
    tags=["example"],
) as dag:
    fetch_data = PythonOperator(
        task_id="fetch_data",
        python_callable=fetch_data,
    )

    analyze_data = PythonOperator(
        task_id="analyze_data",
        python_callable=analyze_data,
    )

    fetch_data >> analyze_data
