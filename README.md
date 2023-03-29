# Appsmith Lightning Datasources

We know that setting up Datasources in Appsmith is fast and easy, but sometimes setting up the services you want to connect to is not as easy.

This project aims to provide fast and easy steps to set up such services so that you can get to hacking around with Appsmith as soon as possible.

## Notes

- The deployment instructions provided here are not suited for production use, please use them for testing and POCs only.
- On Linux, docker commands must be run as administrator.
- If you are deploying this on a hosting provider, you will need to use `Ngrok` to get a usable URL to connect to. If you use this locally, just remember to use `localhost`.
- Example how to get Ngrok host and port to make connections.
```console
appsmith@ngrok:~$ ngrok tcp 3306
Session Status   
online                                                                                   
Account                       Appsmith-svg (Plan: Free)                                                                  
Version                       3.1.0                                                                                     
Region                        Europe (eu)                                                                               
Latency                       164ms                                                                                    
Web Interface                 http://127.0.0.1:4040                                                                     
Forwarding                    tcp://0.tcp.eu.ngrok.io:16696 -> localhost:3306 
Connections                  
ttl     opn     rt1     rt5     p50     p90                                                                            
0       0       0.00    0.00    0.00    0.00                                                                                 
```

- For example, the host and the port to make that connection would be.

`host: 0.tcp.eu.ngrok.io`
`port: 16696`

## General Requirements

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Ngrok](https://ngrok.com/)


## Service Setup

### 🌿 MongoDB

1. Copy the provided `docker-compose.yaml` [for MongoDB](MongoDB/docker-compose.yaml).

```yaml
version: '3.1'
services:
  mongodb:
    image: mongo:6.0
    restart: always
    container_name: mongodb
    environment:
      MONGO_INITDB_ROOT_USERNAME: appsmith
      MONGO_INITDB_ROOT_PASSWORD: appsmith
    ports:
      - "27017:27017"
```

2. Run the deployment. 

```bash
docker-compose up -d docker-compose.yaml
```
`Note: There is a version that uses a seed, in case you want to test with a DB with data`
```
docker-compose -f docker-compose.seeded.yaml up -d
```
3. Open a terminal and create a reachable URL via Ngrok with the following command.

```bash
ngrok tcp 27017
```
4. Follow our guide to create a [MongoDB Datasource](https://docs.appsmith.com/reference/datasources/querying-mongodb).
    - Use the URL provided by the Ngrok command as the *host* in your connection settings.

5. Happy hacking!




### 🐬 MySQL

1. Copy the provided `docker-compose.yaml` [for MySQL](Mysql/docker-compose.yaml).
```yaml
version: '3.3'
services:
  mysql:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_DATABASE: 'db'
      MYSQL_USER: 'appsmith'
      MYSQL_PASSWORD: 'appsmith'
    ports:
      - '3306:3306'
    expose:
      - '3306'
    volumes:
      - my-db:/var/lib/mysql
volumes:
  my-db:
```
2. Run the deployment. 

```bash
docker-compose up -d docker-compose.yaml
```
`Note: There is a version that uses a seed, in case you want to test with a DB with data`
```
docker-compose -f docker-compose.seeded.yaml up -d
```
3. Open a terminal and create a reachable URL via Ngrok with the following command.

```bash
ngrok tcp 3306
```
4. Follow our guide to create a [MySQL Datasource](https://docs.appsmith.com/reference/datasources/querying-mysql).
   - Use the URL provided by the Ngrok command as the *host* in your connection settings.
   
   `Note: disable the SSL`
   
5. Happy hacking!





### 🐘 PostgreSQL 
1. Copy the provider ` docker-compose.yml`[for PostgreSQL](/Postgress/docker-compose.yaml)
```yaml
version: '3'
services:
  postgres:
          image: 'postgres:12'
          restart: always
          volumes:
          - './postgres_data:/var/lib/postgresql/data'
          environment:
          - POSTGRES_PASSWORD=appsmith
          ports:
          - '5432:5432'
```
2. Run the deployment.
``` bash
docker-compose up -d docker-compose.yaml 
```
`Note: There is a version that uses a seed, in case you want to test with a DB with data`
```
docker-compose -f docker-compose.seeded.yaml up -d
```
3. Open a terminal and create a reachable URL via Ngrok with the following command.
```bash
ngrok tcp 5432
```
4. Follow our guide to create a [PostgreSQL](https://docs.appsmith.com/reference/datasources/querying-postgres).
   - Use the URL provided by the Ngrok command as the *host* in your connection settings.
5. Host and port are given by ngrok
6. Database name
`
postgres
`
7. User
`
postgres
`
8. Password
`
secure_pass_here
`
9. Happy hacking!

###  🟥 Redis

1. Copy the provider docker-compose.yml [for Redis](/Redis/docker-compose.yaml).
```yaml
version: '2'

services:
  redis:
    image: docker.io/bitnami/redis:7.0
    environment:
      - ALLOW_EMPTY_PASSWORD=yes
      - REDIS_DISABLE_COMMANDS=FLUSHDB,FLUSHALL
    ports:
      - '6379:6379'
    volumes:
      - 'redis_data:/bitnami/redis/data'

volumes:
  redis_data:
    driver: local
```
2. Run the deployment.
```bash
docker-compose up -d docker-compose.yaml 
```
3. Open a terminal and create a reachable URL via Ngrok with the following command.
```bash
ngrok tcp 6379
```
4.  Follow our guide to create a [Redis](https://docs.appsmith.com/reference/datasources/querying-redis).
    - Use the URL provided by the Ngrok command as the *host* in your connection settings.
5. Host and port are given by ngrok
6. Happy hacking!

###  ElasticSearch
1. Copy the provider docker-compose.yml [for ElasticSearch](/ElasticSearch/docker-compose.yaml).
```yaml
version: "3.0"
services:
  elasticsearch:
    container_name: es-container
    image: docker.elastic.co/elasticsearch/elasticsearch:7.11.0
    environment:
      - xpack.security.enabled=false
      - "discovery.type=single-node"
    networks:
      - es-net
    ports:
      - 9200:9200
  kibana:
    container_name: kb-container
    image: docker.elastic.co/kibana/kibana:7.11.0
    environment:
      - ELASTICSEARCH_HOSTS=http://es-container:9200
    networks:
      - es-net
    depends_on:
      - elasticsearch
    ports:
      - 5601:5601
networks:
  es-net:
    driver: bridge
```


` Note: This installation may take a long time. `


2. Run the deployment.
```bash
docker-compose up -d docker-compose.yaml 
```
3. Open a terminal and create a reachable URL via Ngrok with the following command
```bash 
ngrok http 9200
```
4. Follow our guide to create a  form ElasticSearch [ElasticSearch](https://docs.appsmith.com/reference/datasources/querying-elasticsearch).
   - Use the URL provided by the Ngrok command as the *host* in your connection settings.
6. The port for the connection is ` 443 `
7. Happy hacking!

### SqlServer

1. Copy the provider docker-compose.yml [for SqlServer](/SqlServer/docker-compose.yaml).
```yaml
version: '3.9'
services:
  mssql:
    image: mcr.microsoft.com/mssql/server:2017-CU31-ubuntu-18.04
    ports:
      - 1433:1433
    volumes:
      - ~/apps/mssql/data:/var/lib/mssqlql/data
    environment:
      - ACCEPT_EULA=Y
      - SA_PASSWORD=Appsmith1!
```
2. Run the deployment.
```bash
docker-compose up -d docker-compose.yaml 
```
`Note: There is a version that uses a seed, in case you want to test with a DB with data`
- Navigate to the path sqlserver/seeded
  ```bash
  cd sqlserver/seeded
  ```
- Run the command.
  ```
  docker-compose -f docker-compose.seeded.yaml up -d
  ```
3. Open a terminal and create a reachable URL via Ngrok with the following command.
```bash
ngrok tcp 1433 
```
4. Follow our guide to create a [SqlServer](https://docs.appsmith.com/reference/datasources/querying-mssql)
   - Use the URL provided by the Ngrok command as the *host* in your connection settings.
5. default database name: ` master `
6. Username: `sa`
7. Password: ` Appsmith1! `
8. Happy hacking!

### 📧 SMTP 

1. Copy the provider docker-compose.yml [for SMTP](/SMTP/docker-compose.yaml)
```yaml
version: '3'
services:
  mail:
    image: bytemark/smtp
    restart: always
    ports:
     - "25:25"
    environment:
      RELAY_HOST: smtp.gmail.com
      RELAY_PORT: 587
      RELAY_USERNAME: appsmith
      RELAY_PASSWORD: appsmith
```
2. Run the deployment.
```bash
docker-compose up -d docker-compose.yaml
```
3.  Open a terminal and create a reachable URL via Ngrok with the following command.
```bash
 ngrok tcp 25 
```
4. Follow our guide to create an [SMTP](https://docs.appsmith.com/reference/datasources/using-smtp)
    - Use the URL provided by the Ngrok command as the *host* in your connection settings.
5. The password and username are ` appsmith`
6. Happy hacking!

### 🥑 ArangoDB
1. Copy the provider docker-compose.yml [for ArangoDB](/ArangoDB/docker-compose.yaml)
```yaml
version: '3.7'
services:
  arangodb_db_container:
    image: arangodb:3.2.2
    environment:
      ARANGO_ROOT_PASSWORD: appsmith
    ports:
      - 8529:8529
```
2. Run the deployment.
```bash
docker-compose up -d docker-compose.yaml 
```
`Note: There is a version that uses a seed, in case you want to test with a DB with data`
```
docker-compose -f docker-compose.seeded.yaml up -d
```
3. Open a terminal and create a reachable URL via Ngrok with the following command.
 ```bash
ngrok tcp 8529
```
4. Follow our guide to create an [ArangoDB](https://docs.appsmith.com/reference/datasources/querying-arango-db)
   - Use the URL provided by the Ngrok command as the *host* in your connection settings.
5. Database name:` _system`
6. User: `appsmith`
7. Password: `appsmith `
# Configuring other data sources 

### ➡️DynamoDB

1. Create an AWS [account](https://portal.aws.amazon.com/billing/signup#/start/email)
2. Enter the AWS shell, whether it is the cloud or the local
3. copy this command to create a table
```console
aws dynamodb create-table --table-name Music --attribute-definitions AttributeName=Artist,AttributeType=S AttributeName=SongTitle,AttributeType=S --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 --table-class STANDARD
```
4. We will verify that the table is active with the following command
```console 
aws dynamodb describe-table --table-name Music | grep TableStatus
```
5. Get your access credentials and your region
6. Follow our guide to create a [DynamoDB](https://docs.appsmith.com/reference/datasources/querying-dynamodb)
### 🪁 S3
1. Create an AWS [account](https://portal.aws.amazon.com/billing/signup#/start/email)
2. Enter the AWS shell, whether it is the cloud or the local
3. We create a s3 bucket: `aws s3 mb s3://bucket-appsmith `
4. We list our buckets: `aws s3 ls `
5. Follow our guide to create a [S3](https://docs.appsmith.com/reference/datasources/querying-amazon-s3)

### 🔥 Firestore

1. We install [Gcloud](https://cloud.google.com/sdk/docs/install?hl=es-419)
2. We will follow the following commands.
3. We create a new project.
` gcloud projects create appsmithfirestore`
4. We list the project.
`gcloud project list `
5. We select the project
`gcloud config set project appsmithfirestore `
6. We create an application
`gcloud app create `
7. Create the database
`gcloud firestore databases create --region=us-east1 `
8. Database URL ` https://appsmithfirestore.firebaseio.com`
9. Follow our guide to creating a [Firestore](https://docs.appsmith.com/v/v1.2/datasource-reference/querying-firestore)


