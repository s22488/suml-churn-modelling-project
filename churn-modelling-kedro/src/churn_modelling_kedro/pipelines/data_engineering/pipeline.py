"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.5
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import process_data, load_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_data,
            inputs=None,
            outputs="raw_data",
            name="load_csv_file"
        ),
        node(
            func=process_data,
            inputs="raw_data",
            outputs="processed_data",
            name="process_data"
        ),
    ])