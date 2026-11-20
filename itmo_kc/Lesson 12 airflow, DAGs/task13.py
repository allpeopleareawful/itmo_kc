from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models import Variable
from datetime import datetime, timedelta
import random


def choose_branch():
    var = Variable.get('is_startml')
    if var == "True":
        return "startml_desc"
    else:
        return "not_startml_desc"

def startmlcourse():
    print("StartML is a starter course for ambitious people")

def notstartmlcourse():
    print("Not a startML course, sorry")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="hw_13_egor-kozlov-bjc-3489",
    start_date=datetime(2022, 1, 1),
    schedule=timedelta(days=1),
    default_args=default_args,
    catchup=False,
    tags=["example"],
) as dag:
    before_branching = DummyOperator(task_id="before_branching")
    determine_course = BranchPythonOperator(task_id="determine_course",
                                            python_callable=choose_branch)
    startml = PythonOperator(
        task_id="startml_desc",
        python_callable=startmlcourse,
    )

    not_startml = PythonOperator(
        task_id="not_startml_desc",
        python_callable=notstartmlcourse,
    )

    after_branching = DummyOperator(task_id="after_branching",
                                    trigger_rule="none_failed_min_one_success")

    before_branching >> determine_course >> [not_startml, startml] >> after_branching
