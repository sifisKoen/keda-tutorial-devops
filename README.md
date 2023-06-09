# KEDA-Tutorial-DEVOPS

![TutorialDiagram](tutorial-keda/final-step/KEDA-tutorial-Diagram.png)

## Tuorial

You can find the tutorial in this page.
[Killercoda Tutorial](https://killercoda.com/iosif-koen/scenario/tutorial-keda)

## What we will need ⏩

- Create a new Flask application.
  - Include into Flask application **prometheus_flask_exporter** library.
- Upload our Flask application to Docker Hub.
- Install **KEDA** to our Kubernetes project.
- Create a new **KEDA** scale object.
- Create a **Prometheus** configuration yaml file.
- Finally create a **K6** testing script so to test our application with virtual users.

---

## What we have ☑️

- [x] Create our Flask application. (Plus subsection)
- [x] Upload our Flask application to Docker Hub.
  - [iosifkoen/keda_server_tutorial:latest]
- [x] Install **KEDA** to our Kubernetes project.
- [x] All the steps above.

---

## What we have but need to be tested 🪛

- [x] **KEDA** yaml for scalable object.
- [x] **Prometheus** configuration yaml file.

---

## TODO 💻

- [x] **K6** testing script.

[iosifkoen/keda_server_tutorial:latest]: https://hub.docker.com/repository/docker/iosifkoen/keda_server_tutorial/general
