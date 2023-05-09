# Deploy to Kubernetes

In this step we will deploy our container to our kubernetes cluster. So to use the **KEDA** tool to our cluster.

## Create Our POD 🥛

Firstly we need to deploy our container to our kubernetes cluster inside a POD.

To do this we will need to create our pod using our docker container from previous slide. 😃

This is our container: 👉 `iosifkoen/keda_server_tutorial:latest`

To create the POD you will need a _YAML_ file,

Do not worry about that we have already created one for you. The only thing you need to do it to run this _YAML_ file. The command is very simple, and you have just to click the command bellow.

````
kubectl apply -f server-pod.yaml
```{{exec}}

Now you have your server pod up and running in the *Kubernetes* cluster.

> NOTE: You can see the pod you need to use this command: `kubectl get pods -o wide`.

---

## Exposing to the world

So far we know that we have our image in *Docker Hub* and we can have run this image in a container in a pod in our *Kubernetes* cluster. But now it's time to expose our pod to the real world so access it, and be able to see our webpage.

We gonna use a command for this purpose.

First of all we can see only the half command here the only thing you have to do is to copy this command and paste it into the command line and tap the **TAB** button.

````

kubectl expose pod server

```

What happened now was that because we don't know exactly the name of the pod in the cluster we use the **TAB** for the autocomplete.

Now that we have the first part of our command the only thing is to specify our flags. Copy these flags into the terminal.


```

--name=exposed-server-pod --port=8080 --type=NodePort

```

**Congratulations !** You have created your own service witch is used to expose your pod.

So to see your service execute this command.

```

kubectl get services -o wide

```{{exec}}

Now you should see the service that we have build. *exposed-server-pod* Under the *PORT(s)* column you should some ports and one filed like `8080:30520/TCP`. From this area you need to copy only the second part `30520` (in your case that should be different port). Now you need to go to the upper corner To the burger (🍔) menu and click the the *Traffic/Port* from there you can paste this port to the field and you will be able to see the web page from the pod.

> No you have the complete command witch it should be like this: `kubectl expose pod server-5458d48554-7wc74 --name=exposed-server-pod --port=8080 --type=NodePort` except the `server-5458d48554-7wc74` witch it should be your own pod.

### Explanation

A brief explanation of the flags.

* `--name=exposed-server-pod` This flag is used to give a name to our service in this example we used *exposed-server-pod*
* `--port=8080` This flag is used to specify the port of the pod we are listening on.
* `--type=NodePort` Finally this flag is used to specify what type will gonna be our service.

```
