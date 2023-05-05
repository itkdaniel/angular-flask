"# angular-flask" 

Create virtual environment for python backend

In ./backend run 

`/backend$: python -m venv project_env`

`/backend$: project_env\Scripts\activate`

`/backend$: pip install -r requirements.txt`

Create/Run docker postgresql container

`docker run --name online-exam-db -p 5432:5432 -e POSTGRES_DB=online-exam -e POSTGRES_PASSWORD=0NLIN3-ex4m -d postgres`

Test db entities

`(venv)../backend$: python -m src.main`

Stop docker container

`$ docker stop container-name`

View all containers and confirm status

`$ docker ps -a`

Remove/Delete container

`$ docker rm container_name`

