from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='hw_egor-kozlov-bjc3489_7',
    description='hw for step07',
    schedule=timedelta(days=1),
    start_date=datetime(2026, 10, 13),
    default_args=default_args,
    catchup=False,
    doc_md=dedent("""
        # Title
        **bold**
        *italic*
        `code`
    """),
) as dag:


  def print_func(ts, run_id, **kwargs):
    print(f"task number is: {kwargs['task_number']}")
    print(ts)
    print(run_id)

    return

  for i in range(10, 30):
    t2 = PythonOperator(
        task_id=f'python_{i}',
        python_callable=print_func,
        op_kwargs={'task_number': i},
    )
    t2.doc_md=dedent("""
                        # Title
                        **bold**
                        *italic*
                        `code`
                    """)

    t2
