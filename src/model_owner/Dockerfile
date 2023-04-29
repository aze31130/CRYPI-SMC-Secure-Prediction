FROM python:3.12.0a7-alpine3.17
RUN apk add bash
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY main.py /app
CMD ["python3", "main.py"]