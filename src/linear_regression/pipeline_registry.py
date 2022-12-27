"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from linear_regression.pipelines import training
from linear_regression.pipelines import predict


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    training_pipeline = training.create_pipeline()
    predict_pipeline = predict.create_pipeline()

    return {
        "__default__": training_pipeline,
        "training": training_pipeline,
        "predict": predict_pipeline,
    }