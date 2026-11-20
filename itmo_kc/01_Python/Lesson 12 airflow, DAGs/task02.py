'''
# some dag02
__bold__
*italic*
'''
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta
from textwrap import dedent

default_args = {
    'depends_on_past': False,            # РЅРµ Р·Р°РІРёСЃРµС‚СЊ РѕС‚ СЂРµР·СѓР»СЊС‚Р°С‚Р° РїСЂРµРґС‹РґСѓС‰РµРіРѕ Р·Р°РїСѓСЃРєР°
    'email': ['airflow@example.com'],    # РєРѕРјСѓ РѕС‚РїСЂР°РІР»СЏС‚СЊ СѓРІРµРґРѕРјР»РµРЅРёСЏ
    'email_on_failure': False,           # РЅРµ СЃР»Р°С‚СЊ email РїСЂРё РѕС€РёР±РєРµ
    'email_on_retry': False,             # РЅРµ СЃР»Р°С‚СЊ email РїСЂРё РїРѕРІС‚РѕСЂРЅРѕРј Р·Р°РїСѓСЃРєРµ
    'retries': 1,                        # СЃРєРѕР»СЊРєРѕ СЂР°Р· РїРѕРІС‚РѕСЂСЏС‚СЊ Р·Р°РґР°С‡Сѓ РїСЂРё РѕС€РёР±РєРµ
    'retry_delay': timedelta(minutes=5), # Р·Р°РґРµСЂР¶РєР° РјРµР¶РґСѓ РїРѕРІС‚РѕСЂР°РјРё
}

with DAG(
    dag_id='hw_egor-kozlov-bjc3489_2',
    description='hw for step02',
    schedule=timedelta(days = 1),
    start_date=datetime(2026, 10, 13),
    default_args=default_args,
    catchup=False,
    doc_md=__doc__,
) as dag:

    def print_ds(ds):
        print(ds)

        return

    t1 = PythonOperator(
        task_id='print_ds',
        python_callable=print_ds,
        doc_md=dedent('''
        # python DAG
        __bold__
        _italic_
        `python` task'''),
    )

    t2 = BashOperator(
        task_id='check_pwd',
        bash_command='pwd',
        doc_md=dedent('''
        # bash DAG
        **bold**
        *italic*
        `bash` task'''),
    )

    t2 >> t1