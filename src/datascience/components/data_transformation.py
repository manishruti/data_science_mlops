import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
from src.datascience.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config


    def train_test_split(self):
        data = pd.read_csv(self.config.data_file_path)

        # Split the data into training and test sets (0.75, 0.25) split

        train, test = train_test_split(data, test_size=0.25)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into training and test set")
        logger.info(f"train shape:{train.shape}")
        logger.info(f"test.shape:{test.shape}")

        print(train.shape)
        print(test.shape)