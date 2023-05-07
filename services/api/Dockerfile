# Base Image
FROM python:3.9-alpine

RUN apk update && \
	apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install psycopg2 && \
    apk --purge del .build-deps

# set the working directory to /app
WORKDIR /app

# copy requirements file into container at /app
COPY requirements.txt .

# install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set Flask envrionment variable
ENV FLASK_APP=.\src\app.py

# copy the rest of the application code into container at /app
COPY . .

# Expose the port that the API service will run on
EXPOSE 5000

# Start the API service
CMD ["python", "-m", "src.app"]
# CMD ["python", "app.py", "run", "--host", "0.0.0.0", "--port", "5000"]
# flask run --host 0.0.0.0
