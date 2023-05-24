# Config our Prometheus 📡

## Prometheus Image

![Prometheusimg](./Prometheus-Instance.png)

---

For this step we will need to configure our Prometheus and run it as **Docker** container.

First of all you will need to configure the yaml file that we have all ready build for you, it's time to make your hands dirty. 😁

First let's see our file execute this command: `cat prometheus.yaml`

Now you should see the initial configuration of our Prometheus and you can see two areas where you will need to change them. **- targets: [ ' < node-ip >:< node-port > ' ]**

Ok let's start ▶️

## YAML Configuration

### Ip address

First we will change the **< node-ip >** field. Execute this command. `ifconfig` .Now you can see too many IPs we will need the public IP you can find it in the field **enp1s0:** the ip should be `172.30.1.2` at **inet** field. Now copy this address and open our file with the command line editor of your choice. (Vim, Nano)

> ifconfig is not installed by default in your system so you can install it through net-tools. You can ran this command `sudo apt install net-tools` if you are in **Debian based** system, if you are in other system you need to use yours system's package manager. For *Arch* based systems is **pacman**, for *Fedora/RH* based systems is dnf.

> To write to VIM just press the < i > in your keyboard and when you finish and you want to exit just press < ESC > and < :qw! >. (Don't quit the whole tab 😜). 🪺

Perfect now we need to find our Pods service **port number**, so to let **Prometheus** have acess to our Pod.

### Port number

To find the port number, it's very simple just you need to run one command from one of our previous steps. `kubectl get services -o wide`. Yep! Exactly you have already saw this command, just copy the port number from here. The port number should be like this **31147**. Overall a port number from **30000 to 32767**

And now that you have copied the port number you are ready to move forward to the final step for our configuration. Again as before you need to open and configure the **prometheus.yaml** file, and change the filed **<node-port>**.

**Congratulation**! 🥳 You have successfully configured our **prometheus.yaml** configuration file. Now we have one last step for our **Prometheus** deployment.

### Apply our configuration file

Now that we have is only to run our **prometheus.yaml** file as docker file.

Just run the following command.

```cmd
docker run -d --name prometheus -p 9090:9090 -v $(pwd)/prometheus.yaml:/etc/prometheus/prometheus.yml prom/prometheus
```{{exec}}

### Optional step

If you want to to see the Prometheus application you can just go to the upper corner to the burger (🍔) menu and click the the _Traffic/Port_ from there you can type `9090` port and you will be able to see our Prometheus application.

If you you logged in to **Prometheus** now you can execute some Queries so to be sure that the **Prometheus** instance is up and running. You can copy this trivial command so to execute it yourself `flask_exporter_info`.
