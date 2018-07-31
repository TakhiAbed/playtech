FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y software-properties-common 
RUN apt-get update
RUN apt-get install -y build-essential python3 python3-dev python3-pip 
RUN apt-get install -y git
RUN pip3 install django 
RUN pip3 install djangorestframework
RUN git clone https://github.com/TakhiAbed/workassignment.git
WORKDIR "workassignment"
CMD python3 manage.py runserver 0.0.0.0:8000

