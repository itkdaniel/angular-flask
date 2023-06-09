FROM ubuntu:18.04

USER root
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get update -qq \
    && apt-get install -qqy apt-transport-https ca-certificates \
    curl gnupg2 software-properties-common 
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | apt-key add -
RUN add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") \
    stable"
RUN apt-get update -qq \
    && apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

COPY . /angular-flask

WORKDIR /angular-flask

RUN pip install --no-cache-dir pytest

RUN chmod +x testrun.sh

CMD ["/bin/sh","testrun.sh"]

ENTRYPOINT ["tail", "-f", "/dev/null"]

