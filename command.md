# command to check docker images
docker images
# command to build image
docker build -t <imagename>
# command to remove dockerimage
docker rmi <imageid>
# command to create containter
 docker run --name=cup -dp 5002:5002 mary:latest
 # command that determine container that runs
  docker ps -a