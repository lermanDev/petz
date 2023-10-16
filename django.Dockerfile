FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./app /app

RUN apt-get update \
    && apt-get install -y npm \
    && apt-get clean && apt-get -y autoremove

RUN pip3 install poetry

RUN poetry install

RUN poetry run python manage.py tailwind install;
RUN poetry run python manage.py tailwind build;
RUN poetry run python manage.py collectstatic;