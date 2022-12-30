#!/bin/sh

sudo kubectl create namespace seldon-kedro

sudo kubectl apply -f - << END

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
    replicas: 0

END
