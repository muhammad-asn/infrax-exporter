FROM python:3.9-slim

RUN mkdir /app

WORKDIR /app

COPY infrax.py /app
COPY requirements.txt /app
COPY service /app/service

RUN apt-get update && apt-get install -y curl
RUN pip3 install -r requirements.txt

EXPOSE 8001

ENTRYPOINT [ "python3", "infrax.py" ]
