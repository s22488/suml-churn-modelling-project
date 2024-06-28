"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.5
"""

from pandas import DataFrame, read_csv
from sklearn.preprocessing import LabelEncoder


def load_data() -> DataFrame:
    """Load data from csv into dataset"""
    file_name = "churn-data.csv"
    dataset = read_csv(file_name)
    return dataset


def process_data(df: DataFrame) -> DataFrame:
    """Handle missing values"""
    df = df.dropna()  # drop rows with missing values

    # Feature engineering
    df["NewTenure"] = df["Tenure"] / df["Age"]

    print(df)

    lab_enc_2 = LabelEncoder()
    df["Gender"] = lab_enc_2.fit_transform(df["Gender"])

    lab_enc = LabelEncoder()
    df["Geography"] = lab_enc.fit_transform(df["Geography"])

    # Dropping unnecessary variables
    df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

    print(df)

    return df
