FROM python:3.11-alpine

RUN  apk update \
     && apk add gcc python3-dev musl-dev linux-headers \
     && apk add git \
     && pip install poetry 

ENV POETRY_VIRTUALENVS_IN_PROJECT=1

WORKDIR /obmep

COPY pyproject.toml ./
COPY obmep ./obmep

RUN poetry install