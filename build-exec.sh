#!/bin/bash
sudo docker build -t $1 ./ 
if [ "$(sudo docker image ls  $1)" ]
then
 sudo docker run -it -p 4242:4242 -v $(pwd):/app $1
fi