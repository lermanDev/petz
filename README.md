# Pet Adoption CMS
Pet Adoption CMS is an open-source content management system designed for pet adoption organizations. 
This README provides instructions for setting up and running the project using Docker Compose.

## Prerequisites
Before you begin, make sure you have the following installed:

- Docker
- Docker Compose

## Docker Compose

The Docker Compose configurations allows you to easily set up and run the Pet Adoption CMS project. It includes two services:

- **pets-database**: PostgreSQL database server for storing data.
- **pets-diesel-migrate**: A container that runs Diesel migrations to set up the database schema.

## Getting Started to Development

1. Clone this repository to your local machine.

2. Navigate to the project directory.

3. Create a .env file in the project directory with the following environment variables:

    POSTGRES_DB=mydb
    POSTGRES_USER=myuser
    POSTGRES_PASSWORD=mypassword

You can replace `mydb`, `myuser`, and `mypassword` with your preferred database configuration.

## Run development services
Open a terminal and run the following command to start the Docker containers:

    docker-compose -f docker-compose-development.yml up  

`--build` don't do anything at this point
to delete completele all use `docker-compose -f docker-compose-development.yml down`

This will build and start the PostgreSQL database. If it's your first time you need to apply migrations first.

## Applying migrations
To apply migrations, use the following command:

    docker-compose -f docker-compose-migration-run.yml up --build

This command recreates the container from scratch and runs the migrations.

## Accessing the Application
Database: PostgreSQL is running on port 5432 in the Docker container. You can access it using your preferred PostgreSQL client or connect your application to it.

## Stopping the Containers
To stop the Docker containers, open a terminal and press Ctrl+C. This will gracefully stop the containers. You can also use the following command:

    docker-compose -f docker-compose-development.yml down

## Additional Configuration
You can customize the database credentials and other environment variables by editing the `.env` file.

Modify the `docker-compose.yml` file to adjust port mappings or container names according to your project's requirements.

## License
This project is licensed under the MIT License.