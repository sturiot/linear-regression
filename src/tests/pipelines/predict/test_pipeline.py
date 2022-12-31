import pytest
import numpy as np

from linear_regression.api_serving.linear_regression import LinearRegression

def test_pipeline():
    inputs = "{\"ft_1\":3, \"ft_2\":5}"
    expected = 22.0
    actual = round(LinearRegression().predict(inputs)[0], 0)
    assert actual == expected

def main(*args, **kwargs):
    test_pipeline()

if __name__ == "__main__":
    main()