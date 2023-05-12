# Config our Prometheus 📡

For this step we will need to configure our Prometheus and run it as **Docker** container.

First of all you will need to configure the yaml file that we have all ready build for you, it's time to make your hands dirty. 😁

First let's see our file execute this command: `cat prometheus.yaml`

Now you should see the initial configuration of our Prometheus and you can see two areas where we will need to change them. **- targets: [ ' < node-ip >:< node-port > ' ]**

Ok let's start ▶️

### Ip address

First we will find the ** < node-ip >** field. Execute this command. `ip a` .Now you can see too many ips we will need the first ip you can see there **lo:** the ip should be `127.0.0.1`. Now copy this address and open our file with the editor of your choice.

> To write to VIM just press the < i > in your keyboard and when you finish and you want to exit just press < ESC > and < :qw! >

Perfect now we need to find our pods node meaning the pod where we can access our pod.

### Port number

It's very simple just we will run one command from one of our prevues sections. `kubectl get services -o wide`. Yep exactly you have already did it just copy the port number from here. A port number like this **31147** Overall a port number from **30000 to 32767**

And now that you have copy the port number you are ready make the final step for our configuration. Again as before you need to open and configure the **prometheus.yaml** file.

Congratulation! 🥳 You have successfully configured our **prometheus.yaml** configuration file. Now we have one last step for our **Prometheus** deployment.

### Apply our configuration file

Now that we have is only to run our **prometheus.yaml** file as docker file.

Just run the following command.

```cmd
docker run -d --name prometheus -p 9090:9090 -v $(pwd)/prometheus.yaml:/etc/prometheus/prometheus.yml prom/prometheus
```{{exec}}

### Optional step

If you want to to see the Prometheus application you can just go to the upper corner to the burger (🍔) menu and click the the _Traffic/Port_ from there you can type `9090` port and you will be able to see our Prometheus application.
