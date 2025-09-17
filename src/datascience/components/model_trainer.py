import pandas as pd
import os
from src.datascience import logger
from sklearn.linear_model import LogisticRegression
import joblib
from src.datascience.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config

    def train_model(self):
        train_data = pd.read_csv(self.config.train_file_path)
        test_data  = pd.read_csv(self.config.test_file_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x  = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y  = test_data[[self.config.target_column]]

        lr = LogisticRegression(penalty=self.config.penalty, l1_ratio=self.config.l1_ratio)
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))