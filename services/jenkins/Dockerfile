FROM jenkins/jenkins:lts
USER root
RUN apt-get update -qq \
    && apt-get install -qqy apt-transport-https ca-certificates \
    curl gnupg2 software-properties-common 
RUN curl -fsSL https://download.docker.com/linux/debian/gpg \
    | apt-key add -
RUN add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian \
    $(. /etc/os-release && echo "$VERSION_CODENAME") \
    stable"
RUN apt-get update -qq \
    && apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y