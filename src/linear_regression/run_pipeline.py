import sys
from linear_regression import runner
import logging

PIPELINE = '__default__'
ENV = 'base'
EXTRA_PARAMS = None

if len(sys.argv) > 1:
    PIPELINE = sys.argv[1]
    if len(sys.argv) > 2:
        ENV = sys.argv[2]
        if len(sys.argv) > 3:
            EXTRA_PARAMS = sys.argv[3]
logging.getLogger().info('[Run Pipeline] pipeline={}'.format(PIPELINE, ENV))
runner.run_pipeline(pipeline_name = PIPELINE, env = ENV, extra_params = EXTRA_PARAMS)
logging.getLogger().info('[End Pipeline] pipeline={}'.format(PIPELINE, ENV))

