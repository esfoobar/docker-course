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
  - You build an image from a Dockerfile using `docker build`
- Containers
  - Running or not running
    - Use `docker ps` to see running containers and `docker ps -a` to see all containers
    - You start a container using `docker run` or `docker start`
    - You stop a container using `docker stop`
  - Foreground vs Background
    - Foreground: Starts the process in the container and attach the console to the process’s standard input, output, and standard error
    - Background or detached: Containers started in detached mode exit when the root process used to run the container exits
    - Example foreground container
      - Run an Ubuntu server `docker run -it ubuntu:16.04 /bin/bash`
        - Here we pass the `-i` flag which means "Keep STDIN open" i.e., the keystrokes are routed to the container
        - We also pass the '-t' flag which means "Allocate a pseudo-tty" or terminal
        - We pass the image with a version
        - The `/bin/bash` is an optional command we can pass the container when it starts
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
- Just using python hello.py
- Write the Dockerfile
- Build the image with `docker build -t hello-app .`
- Run the container with `docker run -d -p 5000:5000 --name hello-server hello-app`
- Check that the container is running
- Go to `localhost:5000`. You should see `Hello, World!`
- Stop the container using `docker stop hello-server`
- Check that the container is not running with `docker ps`
- Check the container is still available with `docker ps -a`
- You can restart the server using `docker start hello-server`
- You can log in to the server using `docker exec -it hello-server bash`
- Caveat: if you change the code, it's not reflected on the container. We'll fix that next.

#### 2.2 A Gunicorn based app
- Write the Dockerfile
- Build the image with `docker build -t guni-app .`
- Run the container with `docker run -d -p 80:80 -v /opt/docker-course/apps/2.2:/app --name guni-server guni-app`
- Note the `-v` flag. That means now the local directory is "mounted" on the container, and any changes you make are reflected on the server, thanks to the `--reload` flag.

### Section 3 - Docker Compose
### 3.1 What is Docker Compose?
- Docker Compose allows you to programmatically spawn multiple containers specifying the relationship between them
- The [docker-compose.yml](https://docs.docker.com/compose/compose-file/)

### 3.2 A MySQL-based Flask Applications
- Clone the app
- Build the image with `docker-compose build`
- Run the container with `docker-compose up`
- Initialize tables with `docker exec -it counterapp_web_1 python dbinit.py`
- Hit `/` and see the counter incrementing every time you refresh the page
- To use the app container `docker exec -it counterapp_web_1 /bin/bash`
- To use the mysql server do `docker exec -it counterapp_db_1 mysql -uroot -prootpass`
- If you do any changes and need to reset the containers, you can do `docker-compose rm -v`
- Run tests by doing `docker exec -it counterapp_web_1 python tests.py`

### 3.3 A MongoDB-based Flask Application
- In this case we're going to do an application factory with Blueprints
- Clone the app
  - Note that I'm using different container names in docker-compose.yml to avoid conflicts
- Build the image with `docker-compose build`
- Run the container with `docker-compose up`
- Hit `/` and see the counter incrementing every time you refresh the page
- To explore the mongodb database, open a new tab and do `docker exec -it counterapp_db_2 mongo`
  - Do `use counter`, `show collections`, `db.counter.find()`
- To run tests, do `docker exec -it counterapp_web_2 python tests.py`
- Using PDB with Docker Compose
  - Start the database as it's own demon service: `docker-compose up -d db`
  - Now start the application with pdb enabled: `docker-compose run --service-ports web`
  - You will get the live log of just the app and you can stop with CTRL-C
  - Try adding a pdb on the code
  - To stop the db `docker-compose stop db`
