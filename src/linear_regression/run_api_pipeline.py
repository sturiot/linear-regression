import sys
from linear_regression.api_serving.linear_regression import LinearRegression
import logging

PAYLOAD = None

if len(sys.argv) > 1:
    PAYLOAD = sys.argv[1]

logging.getLogger().info('[Run API Pipeline]')
LinearRegression().predict(X = PAYLOAD)
logging.getLogger().info('[End API Pipeline]')

