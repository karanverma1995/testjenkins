FROM ubuntu:17.10
 RUN apt update
 RUN apt upgrade
FROM python:2.7
 ENV PYTHONUNBUFFERED 1
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install --upgrade setuptools 
 RUN pip install -r requirements.txt
 ADD . /code/
 RUN ["apt-get", "update"]
 RUN ["apt-get", "install", "-y", "vim"]
 RUN ["python", "manage.py","makemigrations"]
 RUN ["python", "manage.py","migrate"]
 RUN ["python", "manage.py","runserver","0.0.0.0:80"]
