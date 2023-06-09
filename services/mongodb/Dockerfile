# Use the official MongoDB image as the base image
FROM mongo:latest

# Set environment variables
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=root
ENV MONGO_INITDB_DATABASE=mydatabase

# Expose MongoDB port
EXPOSE 27017

# Set working directory 
#WORKDIR /mongodb

# Copy the initialization script to the working directory
#COPY ./init.sh .

# Copy the initialization script to the Docker image
COPY init.js /docker-entrypoint-initdb.d/

# Grant execute permissions to the initialization script
#RUN chmod +x init.sh

# Grant execute permissions to the initialization script
RUN chmod +x /docker-entrypoint-initdb.d/init.js

# Start MongoDB and run the initialization script
#CMD ["./init.sh"]