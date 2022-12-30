#!/bin/sh

sudo kubectl create namespace seldon

sudo kubectl apply -f - << END

apiVersion: machinelearning.seldon.io/v1alpha2
kind: SeldonDeployment
metadata:
  name: kedro-linear-regression
spec:
  name: seldon
  predictors:
    - graph:
        children: []
        implementation: LINEAR_REGRESSION_SERVER
        modelUri: ' '
        endpoint:
          type: REST
        name: kedro-linear-regression-pipeline-predict
        type: MODEL
      name: kedro-linear-regression-predictor
      replicas: 1


END
