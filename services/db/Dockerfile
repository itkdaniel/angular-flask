FROM postgres:latest

# set environment variables
ENV POSTGRES_DB=online_exam
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

# copy the init script into the container at /docker-entrypoint-initdb.d/
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose port 5432
EXPOSE 5432
