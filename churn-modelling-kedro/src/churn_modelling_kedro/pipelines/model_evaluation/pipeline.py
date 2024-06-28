"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    """Create the model evaluation pipeline."""
    return pipeline([
        node(
            func=evaluate_model,
            inputs="predictions",
            outputs=["evaluation_metrics", "confusion_matrix"],
            name="autogluon_evaluation"
            )
    ])
