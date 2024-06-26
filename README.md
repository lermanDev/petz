# CMS Pet Adoption Project

Welcome to the CMS Pet Adoption Project! This project uses Django and htmx to create a content management system (CMS) focused on pet adoption. It's designed with Docker for easy local development and uses PostgreSQL as its database.

## Pre-requisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/lermandev/pets.git
   cd pets

   ```

2. **Configure environment variables**:

   - Create .env.dev for dev and .env.prod for production in the root directory.
   - Fill in the necessary variables:

   env.dev
   ```env
   POSTGRES_DB=mydb
   POSTGRES_USER=myuser
   POSTGRES_PASSWORD=mypassword

   DEBUG=1
   DJANGO_SQL_ENGINE=django.db.backends.postgresql
   DJANGO_SQL_DATABASE=${POSTGRES_DB}
   DJANGO_SQL_USER=${POSTGRES_USER}
   DJANGO_SQL_PASSWORD=${POSTGRES_PASSWORD}
   DJANGO_SQL_HOST=database
   DJANGO_SQL_PORT=5432
   SECRET_KEY="django-insecure-n5(x*k+%5+g9gu@71#@)o=s3yrxmp%r^vc8wd+8eh5@2emz_5-"
   ```

   env.prod
   ```envPOSTGRES_DB=mydb
   POSTGRES_USER=myuser
   POSTGRES_PASSWORD=mypassword

   DEBUG=0
   DJANGO_SQL_ENGINE=django.db.backends.postgresql
   DJANGO_SQL_DATABASE=${POSTGRES_DB}
   DJANGO_SQL_USER=${POSTGRES_USER}
   DJANGO_SQL_PASSWORD=${POSTGRES_PASSWORD}
   DJANGO_SQL_HOST=database
   DJANGO_SQL_PORT=5432
   SECRET_KEY=your_production_secret_key

   ACME_EMAIL=your_email@example.com
   DJANGO_HOST=demo.petz.es
   DJANGO_ALLOWED_HOSTS=${DJANGO_HOST},localhost,127.0.0.1
   ```

3. **Build and Start Containers**:

   Development
   ```bash
   docker-compose -f docker-compose.dev.yml --env-file .env.dev up --build
   ```

   Production
   ```bash
   docker-compose -f docker-compose.prod.yml --env-file .env.prod up -d
   ```

4. **Migrate the Database**(after the containers have started):

   ```bash
   docker-compose -f docker-compose.dev.yml --env-file .env.dev exec web poetry run python manage.py migrate

   ```

5. **Create Admin**

   ```bash
   docker-compose -f docker-compose.dev.yml --env-file .env.dev exec web poetry run python manage.py createsuperuser
   ```
6. **Create fake data if you want**
   ```bash
   # Create only species and pets with images
   docker-compose -f docker-compose.dev.yml --env-file .env.dev exec web poetry run python manage.py create_test_data --species 5 --pets 10

   # Create all data
   docker-compose -f docker-compose.dev.yml --env-file .env.dev exec web poetry run python manage.py create_test_data --species 5 --characteristics 12 --genders 2 --sizes 3 --shelters 6 --pets 50 --categories 3 --posts 56 --comments 2 --tags 5
   ```
6. **Access the App**:
   - Navigate to http://localhost:8000 in your browser.

## How to Use

- The admin panel can be accessed at http://localhost:8000/admin.
- Add, update, or remove pet adoption listings through the CMS interface.
- Enjoy the ease of use, thanks to htmx.

## Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or propose new features.

## Acknowledgements

This project uses Docker for local development, Docker Compose for multi-container orchestration, and PostgreSQL as its database.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
