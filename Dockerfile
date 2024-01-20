FROM python:3.11-alpine

RUN  apk update \
     && apk add git \
     && pip install poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT=1

WORKDIR /obmep

COPY pyproject.toml poetry.lock ./
COPY obmep ./obmep

RUN poetry install