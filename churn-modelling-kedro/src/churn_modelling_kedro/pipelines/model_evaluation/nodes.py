"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.6
"""

from pandas import DataFrame, crosstab

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def evaluate_model(predictions: DataFrame) -> (DataFrame, DataFrame):
    """Function to evaluate data model"""
    try:
        accuracy = accuracy_score(predictions['Exited'], predictions['Prediction'])
        precision = precision_score(predictions['Exited'], predictions['Prediction'])
        recall = recall_score(predictions['Exited'], predictions['Prediction'])
        f1 = f1_score(predictions['Exited'], predictions['Prediction'])
        confusion_matrix = crosstab(
            predictions['Exited'],
            predictions['Prediction'],
            rownames=['Actual'],
            colnames=['Predicted']
        )

        return DataFrame({
            'accuracy': [accuracy],
            'precision': [precision],
            'recall': [recall],
            'f1_score': [f1]
        }), confusion_matrix

    except KeyError as e:
        print(f"KeyError: {e}. Ensure 'Exited' and 'Prediction' are in predictions_test.")
    except Exception as e:
        print(f"An error occurred: {e}")
