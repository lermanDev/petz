FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./app /app

RUN pip3 install poetry

RUN poetry install

# RUN poetry run python manage.py collectstatic --noinput; 

# in a future for production