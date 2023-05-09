# Install KEDA

First of all we will need to install KEDA to our system.

First you need to follow the instructions/commands that we provide you bellow.

We gonna use the **Helm** repository.

First we will need to create a namespace for keda. It is simple.

```cmd
kubectl create namespace keda
```{{exec}}

Then we need to add the **Helm** repo

```cmd
helm repo add kedacore https://kedacore.github.io/charts
```{{exec}}

After we add the helm repository we gonna need to **Update** the helm repository.

```cmd
helm repo update
```{{exec}}

Final step but very important we gonna need to install the keda Helm chart.

```cmd
helm install keda kedacore/keda --namespace keda
```{{exec}}

> For more information and more ways on how to install KEDA, we strongly suggest to visit the official page so to read more: [KEDA]

[KEDA]: https://keda.sh/docs/2.4/deploy/
