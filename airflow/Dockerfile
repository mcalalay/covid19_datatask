##
#  This dockerfile is used for local development and testing
##
FROM apache/airflow:2.5.0

USER root

RUN sudo apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    python3-distutils \
    libpython3.9-dev

USER airflow

COPY --chown=airflow . .

RUN python -m pip install .


RUN pip install dbt-postgres==1.5.9

RUN dbt deps --project-dir /opt/airflow/example_dbt_project