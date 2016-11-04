## "Essential Docker for Python Flask Development"

### Section 1 - Introduction

#### 1.1 Introduction

- What do we want to accomplish in this course?
- Prerequisites
- What do I need to have to complete this course?

#### 1.2 Introduction to Docker
- What is Docker exactly?

#### 1.3 Installing Docker
- The Docker Clients
  - Docker is available for both Windows and Mac Operating Systems as a native client that utilizes both of those OS’s hypervisor capabilities
- Install Docker for Mac
  - Get dmg
  - Run it
  - Click the Whale to get preferences
  - Go to File Sharing and add "/opt"
- Check the versions

```
$ docker --version
	Docker version 1.12.0, build 8eab29e

$ docker-compose --version
	docker-compose version 1.8.0, build f3628c7

$ docker-machine --version
	docker-machine version 0.8.0, build b85aac1
```

- Check the hello-world container `docker run hello-world`
  - What did just happen?
    - Docker tried to check if it had a hello-world "image"
    - Since it didn't find it, it went to Docker Hub to see if it could find it there
    - It found it and downloaded the "latest" version
    - It then created a "container" based on this image
    - The container ran following the commands on the image's "Dockerfile"

#### 1.4 Docker Concepts
- Images
  - Versions (:version)
- Containers
  - Running or not running
  - Foreground vs Background
    - Foreground: Starts the process in the container and attach the console to the process’s standard input, output, and standard error
    - Background or detached: Containers started in detached mode exit when the root process used to run the container exits
    - Example foreground container
      - Run an Ubuntu server `docker run -it ubuntu:16.04 /bin/bash`
        - Here we pass the `-i` flag which means "Keep STDIN open" i.e., the keystrokes are routed to the container
        - We also pass the '-t' flag which means "Allocate a pseudo-tty" or terminal
  - Example background container
    - Run an nginx web server `docker run -d -p 80:80 --name webserver nginx`
      - Here we pass a `-d` flag, which means "detached" or Background
      - We also pass a '--name' flag, which allows us to reference the container with a name
      - Go to localhost. "Welcome to nginx" should be up
      - Check `docker ps` and you should see the container
      - Stop the container using `docker stop webserver`
- Docker Hub
  - Kind of a Github where you can get images or create and share them
- The Dockerfile
  - It's the recipe to be followed when a container is created
  - It has a lot of commands. No need to learn them all at once, we will be going through some basic ones

### Section 2 - Simple Flask Applications
#### 2.1 A basic Flask App
- Just using python app.py

#### 2.2 A Gunicorn based app
- Interesting [Docker Voting App](https://github.com/docker/example-voting-app/blob/master/vote/Dockerfile)

### Section 3 - Docker Compose
### 3.1 What is Docker Compose?
- Docker Compose allows you to programatically spawn multiple containers specifying the relationship between them
- The docker-compose.yml

### 3.1 A MySQL-based Flask Applications

### 3.2 A MongoDB-based Flask Application
