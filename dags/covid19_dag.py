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
    schedule_interval='*/3 * * * *', #every 3 minutes
    catchup=False  # Do not perform backfill
)


ingest_data_task = BashOperator(
    task_id = 'Bash_task',
    bash_command = 'python $AIRFLOW_HOME/dags/scripts/ingest_and_transform.py',
    dag = dag
    )

dbt_run_task = BashOperator(
    task_id='dbt_run',
    bash_command='cd /app/dbt_project && dbt run',
    dag=dag,
)

ingest_data_task >> dbt_run_task
