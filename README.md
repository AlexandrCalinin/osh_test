# **Project: OSH-test**

* auth_service – Authentication service (user registration and authorization).
* estate_service – Real estate management service (CRUD operations for properties and rooms).

Both services use FastAPI to create a REST API, SQLAlchemy for database interactions, and 
PostgreSQL as the DBMS. The project is containerized using Docker and Docker Compose.

## **Prerequisites**
1. Docker and Docker Compose must be installed on your machine.
2. The project's root directory should contain a .env file with the required environment 
variables (e.g., DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME_AUTH, DB_NAME_ESTATE).

## **Starting the Project**

Build and Run Containers
From the project root directory, execute: ***docker compose up --build***

## **Service Access**

auth_service will be available at: http://localhost:8001
estate_service will be available at: http://localhost:8000

## **Service Descriptions**:

**auth_service**
The authentication service provides an API for user registration and authorization.
Uses PostgreSQL (container auth_db) as the database.

**estate_service**
The real estate management service provides CRUD operations for properties and rooms.
Uses PostgreSQL (container estate_db) for data storage.


## **Technologies**

FastAPI – Creating REST APIs.
SQLAlchemy – ORM for database interactions.
PostgreSQL – Database management system.
Docker and Docker Compose – Containerization and orchestration of services.
Alembic – Database migrations.
Database Migrations
Migration files are located in the migrations directories of each service. Use Alembic to manage database schemas.

## **Logs**
Logs for the estate_service are recorded in the file:
estate_service/estate_service.log

## **Additional Commands**
**Stop containers:**
docker compose down

**Run commands from Taskfile**
task <command_name>