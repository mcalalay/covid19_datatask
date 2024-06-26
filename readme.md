Optional Pre-requisites (softwares):
1) Vagrant
2) Oracle VM Virtual Box

I used spun up a virtual machine to host the applications and to have a clean separate environment to work with for the project.
You can still technically run this in your local machine given it has internet access since the application is containerized.



The tech stack used was vagrant, airflow, dbt, python, and docker.
Vagrant was used to spin up virtual machine so that the necessary configurations were already set and running the environment would be as easy as running a code. (no need to setup and configure a virtual machine again.)
Airflow was used to orchestrate the entire solution so that once it is up and running, there would be less need of overhead maintenance.
DBT is quite new to me yet it has been a popular solution since it uses SQL for ETL/ELT processing and is quite adaptable to your usecase, may it be a cloud solution or on premises server.
Python is quite a common scripting tool amongst its various capabilities, it is the initial step of ingestion in my pipeline.
Containerizing everything and using docker technology has made everything simpler to lift, shift, and deliver.
I used docker-compose to spin up containers for the application to enable it to be run in any sort of environment, may it be the cloud, your local server, or your local computer.



SETUP
1) Spin UP virtual machine
    a) open cmd in  /vagrant_vm/ directory
    b) run in cmd: vagrant init
    c) run in cmd: vagrant up
    d) wait for virtual machine gui to spin up
2) git clone repository
    a) go to a directory you wish to place the repository
    b) run: git clone https://github.com/mcalalay/covid19_datatask.git
3) docker compose up the containers
    a) enter the repository's directory
    b) run: docker compose up -d
    c) wait for all containers to run successfully
    d) access airflow UI by opening a browser and going to localhost:8080
        Airflow Credentials
            username:airflow
            password:airflow
    e) you can manually trigger the dag or wait for its scheduled run every 3 minutes
4) install postgresql in your environment to view/query the data
    a) run: sudo apt update
    b) run: sudo apt install snapd
    c) run: sudo snap install dbeaver-ce
    d) run dbeaver
    e) choose postgresql
        input the following as config for postgresql
            host: localhost
            Database: covid19_project
            user: postgresql
            password: admin


Answers to my activity will be found in the sql_queries directory
One file is made for each question including the explanation inside.
Each query has been used in the data base created.

Room for improvments:
1) documentation can be streamlined and in a better format
2) ELT procedures could have been more complex to produce a more refined data
3) better sql statements could be done (also optimized)
4) better coding principles could have been applied
5) setup can be more automated rather than having to setup a VM and loading some repositories and dependencies
6) could have been deployed to cloud for better adaptability

