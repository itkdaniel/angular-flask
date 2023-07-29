# base image
FROM python:3.9

# install dependencies
RUN apt-get update && apt-get install -y \
	build-essential \
	git \
	python3-pip \
	&& pip3 install -U pip

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod 777 /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app

# set environment variables
ARG PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED 1

# run server
CMD ["/usr/src/app/entrypoint.sh"]

