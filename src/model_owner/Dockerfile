FROM python:latest
# RUN apk add bash gcc
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY main.py /app