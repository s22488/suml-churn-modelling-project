"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.6
"""

import pickle
from typing import Tuple
from pandas import concat, DataFrame
from autogluon.tabular import TabularPredictor, TabularDataset
from sklearn.model_selection import train_test_split


def split_data(df: DataFrame) -> Tuple[DataFrame, DataFrame]:
    """Function to split the data into training and testing sets."""
    train, test = train_test_split(df, test_size=0.1, random_state=42)
    train = TabularDataset(train)
    test = TabularDataset(test)
    return train, test


def train_model(synthetic_train_data: TabularDataset) -> TabularPredictor:
    """Function to train the model on the training data."""
    predictor = (TabularPredictor(label="Exited", eval_metric="balanced_accuracy")
                 .fit(train_data=synthetic_train_data,
                      keep_only_best=True))
    return predictor


def test_model(predictor: TabularPredictor, test_data: DataFrame) -> DataFrame:
    """Function to test the model on the test data."""
    predictions = DataFrame(predictor.predict(data=test_data, as_pandas=True))
    predictions.rename(columns={"Exited": "Prediction"}, inplace=True)
    predictions = concat([predictions, test_data["Exited"]], axis=1)
    return predictions


def save_model(predictor: TabularPredictor):
    """Function to save the model to a pickle file."""
    filename = "predictor.pkl"
    predictor.persist()
    pickle.dump(predictor, open(filename, "wb"))
