#!/bin/sh

python -u manage.py run --host 0.0.0.0 --port 80; python -u manage.py create-collections;
