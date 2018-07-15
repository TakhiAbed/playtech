FROM ubuntu:latest
MAINTAINER abedsarkil12@gmail.com

RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN apt-get update
RUN apt-get install -y build-essential python3 python3-dev python3-pip 
RUN apt-get install -y git
RUN pip3 install django 
RUN pip3 install djangorestframework
COPY ./  /usr/src/testcicd
#CMD python3 manage.py makemigrations 
#CMD python3 manage.py migrate
#CMD python3 /usr/src/testcicd manage.py runserver

