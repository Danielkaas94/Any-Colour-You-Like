
# Link: https://www.youtube.com/watch?v=pTFZFxd4hOI - 27:27

# mkdir hello-docker

# cd hello-docker

# code. 


# node app.js

FROM node:alpine
COPY . /app
WORKDIR /app
CMD node app.js

# docker build -t hello-docker .

# docker image ls

# docker run hello-docker



# docker version

# docker pull yourDockerUsername/hello-docker

# docker image ls


# docker run yourDockerUsername/hello-docker
