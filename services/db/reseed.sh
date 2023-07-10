#!/bin/sh

echo "Recreating the database"
pg_isready
while $? != '0'; do
   sleep 1.0
   pg_isready
done

psql -U postgres -c "DROP DATABASE IF EXISTS online_exams;"
psql -U postgres -c "CREATE DATABASE online_exams;"
psql -U postgres -d online_exams -f "/usr/src/backup.txt"
