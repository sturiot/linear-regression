# Simple Linear Regression With Kedro and Seldon

This repository aims to show how to turn a simple Kedro inference pipeline into a REST microservice using the Seldon Core framework.

The project is composed of two kedro pipelines: a training pipeline and an inference pipeline which will be wrapped and exposed as a micro services with the help of the Seldon framework.

The inference pipeline uses a simple linear regression model (produced by the train pipeline) with the ScikitLearn library.

Very often a model cannot be turned directly into a microservice as it generally requires to perform pre-processing or post-processing tasks. And this is where Kedro comes in!

More info about Kedro here => https://kedro.readthedocs.io/en/stable/index.html

Seldon Quick Start => https://docs.seldon.io/projects/seldon-core/en/latest/nav/getting-started.html

## Model

The input and labelled Data are under the `./data/01_raw` folder.

Target linear regressin calculus:

t_1 = 1 x ft_1 + 2 x ft_2 + 3

**_NOTE:_** a notebook under the `./notebooks` folder is provided to illustrate the calculus.

## Pre-requisites

- Docker + repository in Docker Hub
- Helm
- Kubernetes Cluster
- ISTio
- Seldon Core (https://docs.seldon.io/projects/seldon-core/en/latest/workflow/install.html)

## Installation

- install Istio Gateway
  
  ```bash
  #!/bin/sh

  kubectl apply -f - << END
      apiVersion: networking.istio.io/v1alpha3
      kind: Gateway
      metadata:
      name: seldon-gateway
      namespace: istio-system
      spec:
      selector:
          istio: ingressgateway # use istio default controller
      servers:
      - port:
          number: 80
          name: http
          protocol: HTTP
          hosts:
          - "*"
  END
  ```

- install Seldon Core

  ```bash
  kubectl create namespace seldon-system
  
  helm install seldon-core seldon-core-operator \
      --repo https://storage.googleapis.com/seldon-charts \
      --set usageMetrics.enabled=true \
      --set istio.enabled=true \
      --namespace seldon-system \
      --version 1.12.0
  ```

- setup local port forwarding
  
  Forward a port on your local machine to one in the Kubernetes cluster to access it externally.

  ```bash
  kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
  ```

- build inference pipeline

  ```bash
  #  build
  docker build . -t sturiot/sturiotio:linear-regression-v1.0.2
  
  # push to docker.io
  docker push sturiot/sturiotio:linear-regression-v1.0.2
  ```

- deploy inference pipeline

```bash
#!/bin/sh

kubectl create namespace seldon-kedro

kubectl apply -f - << END

    apiVersion: machinelearning.seldon.io/v1alpha2
    kind: SeldonDeployment
    metadata:
    name: linear-regression
    namespace: seldon-kedro
    spec:
    name: linear-regression-deployment
    predictors:
    - componentSpecs:
        - spec:
            containers:
            - name: linear-regression-pipeline-predict
            image: sturiot/sturiotio:linear-regression-v1.0.2
        graph:
        children: []
        endpoint:
            type: REST
        name: linear-regression-pipeline-predict
        type: MODEL
        name: linear-regression-pipeline-predictor
        replicas: 1

END
```

**_NOTE:_** 

Here the whole inference pipeline will run on a single pod. In other words, all the nodes in the pipeline workflow will be executed on the same pod using the same resources.

If your pipeline requires scalability you should consider converting your Kedro pipeline into something like Kubeflow pipelines where each nodes of the pipeline will run on a dedicated pod using its own resources.

## How to run

```bash
#!/bin/sh

sudo curl -X POST http://localhost:8080/seldon/seldon-kedro/linear-regression/api/v1.0/predictions \
    -H 'Content-Type: application/json' \
    -d '{"strData": "{\"ft_1\":3, \"ft_2\":5}"}'
```

## How to debug and run tests

### Run tests

```bash
# Create conda environment
cond env create -f .src/environment.yml
conda activate default-ml

# run tests
pytest src/tests
```

### Debug

Different launch configurations for VSCode(under `.vcode/launch`) are provided to debug the pipelines using Kedro or the Seldon wrapper.
