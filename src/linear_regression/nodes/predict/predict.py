import logging
from typing import Dict, Tuple

import numpy as np
import pandas as pd

import os
import json
from pathlib import Path
from sklearn.linear_model import LinearRegression

logger = logging.getLogger(__name__)

def load_model(model):
    return model

def predict(model, inputs: []) -> []:
    predictions = model.predict(inputs)
    logger.info(f'predictions: {predictions}')
    return predictions

def parse_payload(ft_1,ft_2) -> []:
    return np.array([[ft_1, ft_2]])

def np_to_pd(model_outputs) -> []:
    return model_outputs, pd.DataFrame(model_outputs, columns=['t_1'])    