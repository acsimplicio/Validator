FROM python:3.11.0-alpine

WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /usr/validator_app/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /usr/validator_app/requirements.txt

COPY . /usr/validator_app/