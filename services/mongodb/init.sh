#!/bin/bash

# Start the MongoDB service
mongod --fork --logpath /var/log/mongodb.log

# Wait for MongoDB to start
sleep 5

# Create the admin user
mongo admin --eval "db.createUser({ user: '$MONGO_INITDB_ROOT_USERNAME', pwd: '$MONGO_INITDB_ROOT_PASSWORD', roles: [{ role: 'root', db: 'admin' }] })"

# Create the database and a sample collection
mongo $MONGO_INITDB_DATABASE --eval "db.myCollection.insertOne({ name: 'John Doe', age: 30 })"

# Shutdown MongoDB
mongod --dbpath /data/db --shutdown
