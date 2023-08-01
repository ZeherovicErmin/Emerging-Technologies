# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

ADD orders.py .

ENV FLASK_APP=orders.py
COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=10000"]