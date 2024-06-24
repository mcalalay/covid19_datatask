FROM apache/airflow:2.2.3

# Install dbt and other required packages
USER root
COPY requirements.txt /requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    && pip install --upgrade pip \
    pip install --no-cache-dir -r /requirements.txt


# Switch back to the airflow user
USER airflow

RUN airflow db init

# Copy the dags folder to the Airflow container
COPY dags/* /opt/airflow/dags
COPY scripts/* /opt/airflow/scripts
COPY dbt_project/* /opt/airflow/dbt_project


# Set the working directory
WORKDIR /opt/airflow

