FROM python:latest

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt app/

RUN pip install -r requirements.txt

COPY . .


