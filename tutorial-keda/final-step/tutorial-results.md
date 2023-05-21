# Tutorial Results

Ok now that our k6 testing tool is running we can see our results.

## Prometheus

First let's go to **Prometheus Dashboard**. Click on the upper corner to the burger (🍔) menu and click the the _Traffic/Port_ from there you can type `9090` port and you will be able to see our Prometheus application.

From here the you can run some queries on the Prometheus. You can run the queries on the textbox _Expression_. You can copy and run this query `flask_http_request_total`, witch we used it also on our **KEDA scaledobject**. And now you can go to **Graph** tab so to the graph of our system and our metrics.

## Kubernetes POD

Finally let's see our pods to scale up. Just open a new **Tab** to our _Killercoda_ environment and run the following command.

```
kubectl get pods -o wide
```
