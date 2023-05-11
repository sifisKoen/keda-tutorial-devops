# KEDA Configuration

Now that we have our **Prometheus** configured and monitor our cluster and we have already installed the **KEDA** we need to configure and spin up **KEDA** for our cluster.

First of all, we need to connect **KEDA** with our **Prometheus** we have already the initial configuration for **KEDA**. If you execute the following command you will be able to see `keda-scaledobject.yaml` just run `ls` (No flags needed).

If you _cat_ the file you will see that we are missing the **serverAddress** area witch need to be updated.

So the only thing you need to do is just to open the file `keda-scaledobject.yaml` with your editor of your choice in the command line and change this field with `0.0.0.0`.

> If you want to copy this configuration file you should need to change this field according to which ip had your Prometheus.

Now you have you configured **KEDA** file it's time to apply the configuration and run **KEDA** for our cluster. Just run the following command.

```cmd
kubectl apply -f keda-scaledobject.yaml
```

Perfect now you have your own **KEDA** instance running into the cluster.
