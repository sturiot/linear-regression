import pytest
import numpy as np
import logging
import pickle

logger = logging.getLogger(__name__)

@pytest.fixture()
def load_model():
    with open("./data/06_models/model.pkl", "rb") as model_file:
        reg_model = pickle.load(model_file)
        logger.info("Model loaded")
        return reg_model      

def test_given_feature_3_5_when_calling_model_then_return_22(load_model):
    inputs = np.array([[3, 5]])
    expected = 22.0
    actual = round(load_model.predict(inputs)[0], 0)
    assert actual == expected
