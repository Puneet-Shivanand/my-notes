docker images 
docker ps -a


docker ps -a 				---gives all docker process/containers
docker images 				---custom docker built images that have been used
docker build -t <name> Folder/. 	---Creates custom docker image from dockerfile


docker run -it -d <name> /bin/bash	---Create and run docker container from image 
docker attach <name>			---attach to specified container name
CTRL+p then CTRL+q			---detach from container
