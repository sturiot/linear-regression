#!/bin/sh

# swagger access with ssh tunnel
# http://localhost:12410/seldon/seldon-kedro/kedro-linear-regression/api/v1.0/doc/#/External%20Ambassador%20API/Predict

sudo curl -X POST http://localhost:8080/seldon/seldon-kedro/kedro-linear-regression/api/v1.0/predictions \
    -H 'Content-Type: application/json' \
    -d '{"strData": "{\"ft_1\":3, \"ft_2\":5}"}'

echo
