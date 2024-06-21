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

# Copy the dags folder to the Airflow container
COPY dags /opt/airflow/dags
COPY .. /app

# Set the working directory
WORKDIR /app
