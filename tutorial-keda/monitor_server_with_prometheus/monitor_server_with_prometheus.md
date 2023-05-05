# Implement prometheus monitoring [![image](https://user-images.githubusercontent.com/49128030/236407404-535f8ce0-0295-4353-b0d2-c490e8d7150f.png)](https://static-00.iconduck.com/assets.00/surveillance-emoji-84x96-2fr11cep.png)


To scrape metrics from our server, which we will later use to scale the clusters, we will need to implement a monitoring system called *Prometheus*. 

## Prometheus 🔥

*Prometheus* is an open-source software used for event monitoring and alerting. It records metrics in a time series database built using an HTTP pull model, with flexible queries and real-time alerting.

## Docker

Again, we will create a Docker image of our Prometheus so we can bake in our configuration into the image to make things easy.

---
## Let's build our Docker container 🪛

Firs let us move to the working directory of our Prometheus.

```
cd prometheus
```{{exec}}

We have already created a Prometheus middleware that exports metrics from our server. What you need to do is build the Prometheus image by clicking the following command.

```
docker build . -t prometheus
```{{exec}}

Now we need to run it so it starts monitoring our server. To do so, click the next command.

```
docker run -p 9090:9090 prometheus
```{{exec}}

**Excellent!!** Now you have implemented Prometheus and are scraping metrics from the server.
