FROM ubuntu:20.04
RUN apt-get update --fix-missing
RUN apt-get upgrade -y --fix-missing
RUN apt-get install -y docker.io
RUN apt-get install -y git
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
RUN npm install semistandard --global
RUN npm install request --global
RUN export NODE_PATH=/usr/lib/node_modules