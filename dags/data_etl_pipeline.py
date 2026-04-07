from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_team',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_callable():
    print(f"Executing extract")

def transform_callable():
    print(f"Executing transform")

def validate_callable():
    print(f"Executing validate")

def load_callable():
    print(f"Executing load")

with DAG(
    dag_id='data_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_callable
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_callable
    )

    validate = PythonOperator(
        task_id='validate',
        python_callable=validate_callable
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_callable
    )

    extract >> transform >> validate >> load
