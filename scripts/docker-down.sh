#!/bin/sh

echo "Stopping and removing containers with docker-compose..."
docker compose down
echo

echo "Removing Docker images..."
docker_images=$(docker images -a -q)
for image_id in $docker_images; do
  echo "Removing image with ID: $image_id"
  docker rmi -f "$image_id"
  echo
done
