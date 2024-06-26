import pandas as pd

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def evaluate_model(predictions: pd.DataFrame,
    project_name='Kedro-SUML-Test-Autogluon',
    learning_rate=0.01,
    epochs=10,
    log_additional_info=True) -> (pd.DataFrame, pd.DataFrame):

    try:
    # Calculating metrics

        accuracy = accuracy_score(predictions['Exited'], predictions['Prediction'])
        precision = precision_score(predictions['Exited'], predictions['Prediction'])
        recall = recall_score(predictions['Exited'], predictions['Prediction'])
        f1 = f1_score(predictions['Exited'], predictions['Prediction'])
        confusion_matrix = pd.crosstab(
            predictions['Exited'],
            predictions['Prediction'],
            rownames=['Actual'],
            colnames=['Predicted']
        )

        return pd.DataFrame({
            'accuracy': [accuracy],
            'precision': [precision],
            'recall': [recall],
            'f1_score': [f1]
        }), confusion_matrix

    except KeyError as e:
        print(f"KeyError: {e}. Ensure 'Exited' and 'Prediction' are in predictions_test.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        run.finish()
