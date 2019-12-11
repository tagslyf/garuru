# create container with debian image with volume
docker run --name debian-garuru -v $(pwd):/usr/src/app/ debian

# install netselect
apt-get update && apt-get install netselect

# install python3 and pip
apt-get update && apt-get install python3-pip
