

docker-compose build
docker-compose up -d
Open your web browser and navigate to http://localhost:8080 to access the Airflow web interface.


Possible errors:
if this is encountered or something similar:
" Airflow "Something Bad Has Happened" Error: Dag Table does not exist "

likely the database needs to be initiated, just follow the steps below:
1) get into the airflow environment and run the following.
    docker ps
    docker exec -it <airflow_container_id> sh
2) run the following command once inside airflow
    airflow db init
    exit
done

if dags won't run, you must do the following commands within the container environment of airflow:

airflow scheduler