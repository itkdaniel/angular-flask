#!/bin/bash
echo "Waiting for postgres..."
while ! nc -z db 5432; do sleep 0.1; done; echo "PostgreSQL started"; python -u manage.py run --host 0.0.0.0 --port 80; python -u manage.py recreate-db;
# python -u manage.py run --host 0.0.0.0 --port 80
# python -u manage.py recreate_db
