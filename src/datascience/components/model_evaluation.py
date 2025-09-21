import os
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score,precision_score,f1_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.utils.common import save_json
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config=config

    def eval_metrices(self, actual, pred):
        acc = accuracy_score(actual, pred)
        recall = recall_score(actual, pred)
        precision = precision_score(actual, pred)
        f1_scores = f1_score(actual, pred)

        return acc, recall, precision, f1_scores

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_file_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Enable autoLogging
        #mlflow.autolog()

        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)
            (acc, recall, precision, f1_score) = self.eval_metrices(test_y, predicted_qualities)

            ## save metrices as local
            scores = {"accuracy": acc, "recall":recall, "precision":precision, "f1_score":f1_score}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("accuacr",acc)
            mlflow.log_metric("recall", recall)
            mlflow.log_metric("precision", precision)
            mlflow.log_metric("f1_score", f1_score)


            # local_model_path = Path("c:/Users/ojha.manish.kumar/Documents/Udemy/DataScience_End_to_End_Projects/mlflow_artifacts").resolve()
            # mlflow.sklearn.save_model(sk_model=model, path=str(local_model_path))

            # mlflow.log_artifacts(str(local_model_path), artifact_path="model")
            mlflow.sklearn.log_model(model, artifact_path="model")
