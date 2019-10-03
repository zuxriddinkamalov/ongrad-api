FROM python:3.7-alpine
MAINTAINER Zukhriddin Kamalov

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN ls -all /
RUN ls -all
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./ /app

RUN adduser -D user
USER user