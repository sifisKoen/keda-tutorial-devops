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

What you need to do is just to build the Docker container. It's very simple. You need just to click the code behind. And the magic will happen. 🪄

```
docker build . -t server
```{{exec}}

Perfect now you have build your Docker container
Now we need to run it so to have access to our page. Click the next command.

```
docker run -dp 8080:8080 server
```{{exec}}

**Perfect!!** Now you have build and run your Docker container.
Now if you want to see the container you can just run the following command.

```
docker ps
```{{exec}}

Now you should see the container in our command line.

[Flask]: https://flask.palletsprojects.com/en/2.3.x/
