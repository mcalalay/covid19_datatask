FROM apache/airflow:2.9.2

# Install dbt and other required packages
USER root
COPY requirements.txt /requirements.txt

RUN apt-get update && apt-get install -y apt-utils

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    && pip install --upgrade pip
USER airflow
RUN python -m pip install dbt-core dbt-postgres

