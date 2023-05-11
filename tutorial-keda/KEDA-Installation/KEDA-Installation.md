# Install KEDA

First of all we will need to install KEDA to our system.

First you need to follow the instructions/commands that we provide you bellow.

We gonna use the **Helm** repository.

First we will need to create a namespace for keda. It is simple.

```cmd
kubectl create namespace keda
```{{exec}}

Then we need to add from the **Helm** repo the Kedacore.

But first we will need to install the **Helm** repo. We will use the the snap command.

```bash
sudo snap install helm --classic
```{{exec}}

> You can find more information about how to install **Helm** here: [Helm Documentation]

```cmd
helm repo add kedacore https://kedacore.github.io/charts
```{{exec}}

As you can see the **Killercoda** has all-ready installed the **Kedacoda**. Although we provide this command for your local machine witch does not have **Kedacoda** installed.

After we add the helm repository we gonna need to **Update** the helm repository.

```cmd
helm repo update
```{{exec}}

Final step but very important we gonna need to install the keda Helm chart.

```cmd
helm install keda kedacore/keda --namespace keda
```{{exec}}

> For more information and more ways on how to install KEDA, we strongly suggest to visit the official page so to read more: [KEDA]

---

# Optional Step

> NOTE: The KEDA pod will start to run after approximately 23 seconds

Finally let us confirm that we have the KEDA operator pod up and running on our namespace.This operator is our operator witch is actually our worker witch poll and config behavior from the Kubernetes Horizontal Pod Autoscaling(HPA) object.

Execute the following commands.

```cmd
kubectl get pod -l app=keda-operator -n keda
```{{exec}}

From this command you should take the **Name** of the pod. Then you will need to copy this name witch will be something like this: `keda-operator-96579d64c-mmwpb`. Actually, the part of **keda-operator** it is exactly the same as in the example. Now you have copied your pod's name you can continue.


`kubectl logs pod/<The name you have copied> -n keda`

> The final command should look like this: kubectl logs pod/keda-operator-96579d64c-mmwpb -n keda

Congratulation 🥳 You now have **KEDA** installed and you can see its logs.

[KEDA]: https://keda.sh/docs/2.4/deploy/
[Helm Documentation]: https://helm.sh/docs/intro/install/
