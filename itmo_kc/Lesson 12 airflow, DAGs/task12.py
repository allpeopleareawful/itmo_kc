from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models import Variable
from datetime import datetime, timedelta
import random


def get_var():
    var = Variable.get('is_startml')
    print(var)
    return var

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="hw_12_egor-kozlov-bjc-3489",
    start_date=datetime(2022, 1, 1),
    schedule=timedelta(days=1),
    default_args=default_args,
    catchup=False,
    tags=["example"],
) as dag:
    get_top = PythonOperator(
        task_id="get_var",
        python_callable=get_var,
    )

    get_top
