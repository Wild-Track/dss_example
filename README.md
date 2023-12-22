# DSS example

## Group

DJERMOUNI - GERARD - POIRE - LAAOUINE

## Required

- Docker
- Python 3

## Set up

To set up this project, simply:

`docker-compose up -d`

This will start the containers (mariaDB and phpMyAdmin).

To populate the database afterward, you'll need to run the Python script with the following command:

`python3 ./import_csv.py`
