from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_team',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='market_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

extract = PythonOperator(
    task_id='extract',
    python_callable=lambda: print(f"Executing extract"),
    dag=dag,
)

transform = PythonOperator(
    task_id='transform',
    python_callable=lambda: print(f"Executing transform"),
    dag=dag,
)

validate = PythonOperator(
    task_id='validate',
    python_callable=lambda: print(f"Executing validate"),
    dag=dag,
)

load = PythonOperator(
    task_id='load',
    python_callable=lambda: print(f"Executing load"),
    dag=dag,
)

extract >> transform >> validate >> load
