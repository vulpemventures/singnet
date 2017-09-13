FROM python:3

MAINTAINER Christian Jensen <christian@jensenbox.com>

ENV PYTHONUNBUFFERED 1
# Install.
#RUN \
#  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
#  apt-get update && \
#  apt-get -y upgrade && \
#  apt-get install -y build-essential && \
#  apt-get install -y software-properties-common && \
#  apt-get install -y byobu curl git htop man unzip vim wget python3.6 && \
#  rm -rf /var/lib/apt/lists/*

RUN mkdir /agent
WORKDIR /agent
ADD . /agent
RUN pip install -r requirements.txt
