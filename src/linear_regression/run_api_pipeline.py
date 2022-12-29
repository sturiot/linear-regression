import sys
from linear_regression.api_serving.linear_regression import LinearRegression
import logging

PAYLOAD = None
ENV = None

if len(sys.argv) > 1:
    PAYLOAD = sys.argv[1]
    if len(sys.argv) > 2:
        ENV = sys.argv[2]

logging.getLogger().info('[Run API Pipeline]')
api_pipeline = LinearRegression(env=ENV)
api_pipeline.predict(X = PAYLOAD)
logging.getLogger().info('[End API Pipeline]')

