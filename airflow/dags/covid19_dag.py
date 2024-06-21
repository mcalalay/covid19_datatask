from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'covid19_ingestion_transformation',
    default_args=default_args,
    description='Ingest and transform COVID-19 data',
    schedule_interval=timedelta(days=1),
)

def ingest_data():
    os.system("python /app/scripts/ingest_data.py")

ingest_data_task = PythonOperator(
    task_id='ingest_data',
    python_callable=ingest_data,
    dag=dag,
)

dbt_run_task = BashOperator(
    task_id='dbt_run',
    bash_command='cd /app/dbt_project && dbt run',
    dag=dag,
)

ingest_data_task >> dbt_run_task
