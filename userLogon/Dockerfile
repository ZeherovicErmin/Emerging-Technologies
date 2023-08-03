# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

ADD userLogon.py .

ENV FLASK_APP=userLogon.py
COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=11000"]