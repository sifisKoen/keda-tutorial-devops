# Deploy our server 🖥️

Well for our tutorial we need to spin off a server and a testing landing page.

## Server 💻

Our server is a basic _Flask_ server. We use this server so to land out html page.

The _Flask_ is python framework if you want to read moore follow this link: [Flask]

## HTML 🌐

We used a very simple HTML page just for our tutorial purpose.

## Docker 🐳

Finally we need to create a Docker container so to spin our server and our page.

We use a Docker container so do not need to install all the dependencies of our project/server

---

## Let's build our Docker container 🪛

We have all ready created the _server, landing page and the Dockerfile_ for you. You don't need to create nothing we got you 😄

What you need to do is just to run the Docker container. It's very simple. You need just to click the code behind. And the magic will happen. 🪄

```
docker run -dp 8080:8080 iosifkoen/keda_server_tutorial
```{{exec}}

**Perfect!!** Now you have build and run your Docker container, from the docker hub. You can find the docker hub repository here: [docker-container]

Now if you want to see the container you can just run the following command.

```
docker ps
```{{exec}}

Now you should see the container in our command line.

If you want to see how to push you own container to **docker hub** you can see the Docker documentation page: [docker-documentation]

[Flask]: https://flask.palletsprojects.com/en/2.3.x/
[docker-container]: https://hub.docker.com/repository/docker/iosifkoen/keda_server_tutorial/general
[docker-documentation]: https://docs.docker.com/

