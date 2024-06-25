"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model, test_model, split_data, save_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs="processed_data",
            outputs=["train_data", "test_data"],
            name="split_data_node"
        ),
        node(
            func=train_model,
            inputs="train_data",
            outputs="predictor",
            name="predictor_creation"
        ),
        node(
            func=test_model,
            inputs=["predictor", "test_data"],
            outputs="predictions",
            name="predictions_creation"
        ),
        node(
            func=save_model,
            inputs=["predictor"],
            outputs=None,
            name="model_saving"
        ),
    ])