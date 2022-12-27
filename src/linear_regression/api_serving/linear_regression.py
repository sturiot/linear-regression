import logging
import json
import pickle
from kedro.framework.project import configure_project
from kedro.framework.session import KedroSession
from typing import Any, Dict

logger = logging.getLogger(__name__)


class LinearRegression(object):
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """

    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """


        logger.info("Initializing")
        project_name = 'linear_regression'
        configure_project(project_name)
        with KedroSession.create() as session:
            self._model = session.run(pipeline_name='predict', node_names=['load_model'])      
        logger.info("Initialized")

    def predict(self, X, features_names=None):
        """
        Return a prediction.

        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        logger.info("Predict called.")
        extra_params = json.loads(X)
        with KedroSession.create(extra_params=extra_params) as session:
            outputs = session.run(pipeline_name='predict', from_nodes=['parse_payload'], to_nodes=['convert_np_pd'])
            return outputs['pipeline_outputs']            
