import logging
from typing import Dict, Tuple

import numpy as np
import pandas as pd

import os
from pathlib import Path
from sklearn.linear_model import LinearRegression

def clean_data(data_x: pd.DataFrame, data_y: pd.DataFrame) -> Tuple:
    data_x.rename(columns = {'ft_1':'X_0', 'ft_2':'X_1'}, inplace = True)
    data_y.rename(columns = {'t_1':'Y_0'}, inplace = True)
    return data_x, data_y

def pd_to_np(data_x: pd.DataFrame, data_y: pd.DataFrame) -> Tuple:
    return data_x.to_numpy(int), data_y.to_numpy(int)


def add_noise(data_x: np.ndarray, data_y: np.ndarray) ->  np.ndarray:
    lamda_func = lambda x: np.dot(x, np.array([1, 2]) + np.random.rand()) + 3
    data_y_with_noise = lamda_func(data_x)
    return data_y_with_noise

def train(data_x: np.ndarray, data_y: np.ndarray):
    return LinearRegression().fit(data_x, data_y)

def save_model(model):
    pass
 