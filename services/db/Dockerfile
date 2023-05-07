FROM postgres:latest

# set environment variables
ENV POSTGRES_DB=online_test
ENV POSTGRES_PASSWORD=0NLIN3-ex4m

# copy the init script into the container at /docker-entrypoint-initdb.d/
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose port 5432
EXPOSE 5432
