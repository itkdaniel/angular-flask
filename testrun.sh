#!/bin/sh

 echo "Check current working directory"
 pwd

 echo "Starting all services"
 docker compose -f docker-compose.yml up -d
 
 docker compose exec api pytest -v src/test --junitxml=reports/result.xml
 echo "Copy result.xml into Jenkins container"
 
 rm -rf reports
 mkdir reports
 
 docker cp angular-flask-api-1:/api/reports/result.xml reports/
 echo "Cleanup"
 
 docker compose down
 /bin/sh scripts/docker-down.sh
