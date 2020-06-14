FROM python:3.6-slim

RUN apt-get -y update && \
    apt-get install -y --no-install-recommends build-essential python-pip python-dev wget nginx libcurl4-openssl-dev libssl-dev procps

COPY . /opt/program

RUN pip install -r /opt/program/requirements.txt

ENV PATH="/opt/program:${PATH}"

WORKDIR /opt/program