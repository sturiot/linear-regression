import logging
import json
import pickle
import seldon_core
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
        self.project_name = 'linear_regression'
        self.pipeline_name = 'predict'
        self.env = None
        configure_project(self.project_name)
        self._load_model()
        logger.info("Initialized")

    def _load_model(self):
        with KedroSession.create(env=self.env) as session:
            self._model = session.run(pipeline_name=self.pipeline_name, node_names=['load_model']) 

    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value       

    @property
    def pipeline_name(self):
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, value):
        self._pipeline_name = value 

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value 

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
        with KedroSession.create(env=self.env, extra_params=extra_params) as session:
            outputs = session.run(pipeline_name=self.pipeline_name, from_nodes=['parse_payload'], to_nodes=['convert_np_pd'])
            return outputs['pipeline_outputs']            
