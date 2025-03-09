# command to check docker images
docker images
# command to build image
docker build -t <imagename>
# command to remove dockerimager
docker rmi <imageid>
# command to create containter
 docker run --name=cup -dp 5002:5002 mary:latest

 docker run --name fountain -dp 5003:5003 mary:latest
 # command that determine container that runs
  docker ps -a