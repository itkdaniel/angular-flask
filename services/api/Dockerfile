# Base Image
FROM python:3.9-alpine

RUN apk update && \
	apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    apk add --no-cache netcat-openbsd && \
    apk add --no-cache curl && \
    apk add --no-cache python3-dev libstdc++ && \
    apk add --no-cache g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip install psycopg2 && \
    apk --purge del .build-deps

RUN mkdir -p /api

# set the working directory to /api
WORKDIR /api

# copy requirements file into container at /api
COPY requirements.txt .

# install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set Flask envrionment variable
# ENV FLASK_APP=manage.py

ENV APP_SETTINGS=src.config.DevelopmentConfig

ENV UPLOAD_DIR=src/api/uploaded_files

ENV JENKINS_DATABASE_URL=postgresql://postgres:postgres@172.17.0.2:5432/online_exam
ENV JENKINS_MONGO_URL=mongodb://root:root@172.17.0.3:27017/mydatabase?authSource=admin
ENV JENKINS_DATABASE_TEST_URL=postgresql://postgres:postgres@172.17.0.2:5432/online_exam_test
ENV JENKINS_MONGO_TEST_URL=mongodb://root:root@172.17.0.3:27017/mydatabase_test?authSource=admin

#ENV JENKINS_DATABASE_URL=postgresql://postgres:postgres@db:5432/online_exam
#ENV JENKINS_MONGO_URL=mongodb://root:root@mongodb:27017/mydatabase?authSource=admin
#ENV JENKINS_DATABASE_TEST_URL=postgresql://postgres:postgres@db:5432/online_exam_test
#ENV JENKINS_MONGO_TEST_URL=mongodb://root:root@mongodb:27017/mydatabase_test?authSource=admin

# REDIS_OM_URL=redis://default:<password>@<host>:<port>

ENV MONGODB_INITDB_ROOT_USERNAME=root
ENV MONGODB_INITDB_ROOT_PASSWORD=root
ENV MONGODB_AUTH_SOURCE=admin
ENV MONGODB_USERNAME=root
ENV MONGODB_PASSWORD=root
ENV MONGODB_DB=mydatabase
ENV MONGODB_HOST=mongodb
ENV MONGODB_PORT=27017
ENV MONGO_INITDB_DATABASE=mydatabase
ENV SECRET_KEY=lostinthesauce

# copy entrypoint file into container at /api
COPY entrypoint.sh .
RUN chmod 777 entrypoint.sh

# copy the rest of the application code into container at /api
COPY . /api

# set environment variables
ARG PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED 1

# Expose the port that the API service will run on
# EXPOSE 5000

# Start the API service
#CMD ["entrypoint.sh"]
CMD ["/bin/sh", "entrypoint.sh"]
# CMD ["python", "-u", "manage.py", "run", "0.0.0.0", "--port", "5000"]
# CMD ["python", "-m", "src.app"]
# CMD ["python", "app.py", "run", "--host", "0.0.0.0", "--port", "5000"]
# flask run --host 0.0.0.0
