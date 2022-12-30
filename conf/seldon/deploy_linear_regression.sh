#!/bin/sh

sudo kubectl create namespace seldon-kedro

sudo kubectl apply -f - << END

apiVersion: machinelearning.seldon.io/v1alpha2
kind: SeldonDeployment
metadata:
  name: kedro-linear-regression
  namespace: seldon-kedro
spec:
  name: seldon-kedro
  predictors:
    - graph:
        children: []
        implementation: LINEAR_REGRESSION_SERVER
        modelUri: gs://seldon-models/v1.15.0-dev/sklearn/iris
        endpoint:
          type: REST
        name: kedro-linear-regression-pipeline-predict
        type: MODEL
      name: kedro-linear-regression-predictor
      replicas: 1


END
