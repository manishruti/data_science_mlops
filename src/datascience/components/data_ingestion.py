## DataIngestion Components
import os
from urllib import request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import DataIngestionConfig

## Downloading csv
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download with following info:\n{headers}")
        else:
            logger.info(f"File already exists")

    def extract_zip_file(self):
        """"
        zip_file_path:str
        Extracts the zip file into the data directory
        Function return None
        """

        unzip_path = self.config.unzip_dir
        os.makedir(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)