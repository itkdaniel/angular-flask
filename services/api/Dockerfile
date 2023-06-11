# Base Image
FROM python:3.9-alpine

RUN apk update && \
	apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
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
# ENV FLASK_APP=./src/app.py
ENV DATABASE_URL=postgresql://postgres:postgres@localhost:5432/online_exam
ENV MONGO_URL=mongodb://root:root@localhost:27017/mydatabase?authSource=admin

# copy entrypoint file into container at /api
COPY entrypoint.sh .
RUN chmod 777 entrypoint.sh

# copy the rest of the application code into container at /api
COPY . /api

# set environment variables
ARG PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED 1

# Expose the port that the API service will run on
EXPOSE 5000

# Start the API service
CMD ["/bin/sh", "entrypoint.sh"]
# CMD ["python", "-u", "manage.py", "run", "0.0.0.0", "--port", "5000"]
# CMD ["python", "-m", "src.app"]
# CMD ["python", "app.py", "run", "--host", "0.0.0.0", "--port", "5000"]
# flask run --host 0.0.0.0
