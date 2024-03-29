# angular-flask

### Create virtual environment for python backend api

In ./api run 

`/api$: python -m venv venv`

`/api$: venv\Scripts\activate`

`/api$: pip install -r requirements.txt`

Manually Create/Run docker postgresql container

`docker run --name online-exam-db -p 5432:5432 -e POSTGRES_DB=online-exam -e POSTGRES_PASSWORD=0NLIN3-ex4m -d postgres`

### **Alternatively** Start/Stop all services using **docker-compose**

`docker-compose up` to run all services  
`docker-compose down` to stop all services and remove containers

`for /F %i in ('docker images -a -q') do docker rmi -f %i` to remove all images

**OR** `docker rmi imageid ...` to remove images by id

**OR** `docker-down` to stop all services and remove containers/images

**OR** `docker-restart service_name` to stop a service and remove associated container/image

`docker-compose up service_name` to start a specified service

### To Build and run individually

`/db$: docker build -t angular-flask-db --no-cache .`

`/db$: docker run -p 5432:5432 angular-flask-db`

`/api$: docker build -t angular-flask-api --no-cache .`

`/api$: docker run -p 5000:5000 angular-flask-api`

### To enter psql interactivate mode

`docker exec -it angular-flask-db-1 bash`  

`psql -h localhost -U postgres`

Test insert data

`insert into exams values ('Docker Test', 'Test about Docker', 22);`

Exit interactive mode

`\q` then `\exit`

### Test db and api

`(venv)../backend$: python -m src.testdb`

Set FLASK_APP environment variable

`set FLASK_APP=.\src\app.py`

Run Flask api

`/services/api$: python -m src.app`

Navigate to `http://localhost:5000/api/exams` or from cmd `curl http://localhost:5000/api/exams`

### Test using docker-compose

Enter api container/service 

`/angular-flask$: docker-compose exec api pytest -v src/test --junitxml=reports/result.xml`

`/angular-flask$: docker-compose exec -it api /bin/sh`

`/api # python -m unittest -v src.test.test_config`

`/api # python -m unittest discover -v`

### Stop and remove docker containers/images

`$ docker stop container-name`

View all containers and confirm status

`$ docker ps -a`

Remove/Delete containers and images

`$ docker rm container_name ...`
`$ docker rmi imageid ...`

