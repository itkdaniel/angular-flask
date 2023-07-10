FROM postgres:15.3-alpine

# set environment variables
ENV POSTGRES_DB=online_exam
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

# copy the init script into the container at /docker-entrypoint-initdb.d/
COPY ./init.sql /docker-entrypoint-initdb.d/
COPY ./backup.txt /usr/src/backup.txt
COPY ./reseed.sh /usr/src/reseed.sh
RUN chmod 777 /usr/src/reseed.sh

WORKDIR /usr/src

# Expose port 5432
EXPOSE 5432
