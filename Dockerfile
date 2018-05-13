FROM ubuntu:16.04

RUN apt-get -y update &&\
        apt-get -y upgrade &&\
        apt-get -y install python3-pip

RUN pip3 install configparser &&\
        pip3 install pathlib &&\
        pip3 install urllib3

RUN apt-get -y install apache2-utils

ADD . .

EXPOSE 80

CMD python3 main.py