FROM ubuntu:latest

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update
RUN apt-get install python3 python3-pip -y

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential -y
RUN pip install mysqlclient

EXPOSE 5000

COPY ./ ./

CMD ["flask", "run"]