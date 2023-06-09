@echo off
setlocal enabledelayedexpansion

echo Stopping and removing containers with docker-compose...
docker-compose down
echo.

echo Removing Docker images...
for /F %%i in ('docker images -a -q') do (
  set "image_id=%%i"
  echo Removing image with ID: !image_id!
  docker rmi -f !image_id!
  echo.   
)

endlocal
