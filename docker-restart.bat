@echo off

REM Check if an argument is provided
IF "%~1"=="" (
  echo No service name provided. Usage: docker-restart [service_name]
  exit /b 1
)

REM Stop the Docker service
set container_name=angular-flask-%~1-1
echo Stopping Docker service: %container_name%
docker stop %container_name%
echo.

REM Get the container name of the stopped service
FOR /F "tokens=*" %%a IN ('docker ps -a -f "name=%container_name%" --format "{{.Names}}"') DO SET container_name=%%a

REM Remove the container of the stopped service if it exists
IF DEFINED container_name (
  echo Removing container: %container_name%
  docker rm -f %container_name%
)
echo.

REM Get the image repository name associated with the service name
set image_name=angular-flask-%~1
echo Removing image: %image_name%
docker rmi %image_name%
)

echo Docker service restart completed.

exit /b 0
