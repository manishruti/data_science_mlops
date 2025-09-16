from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline



try:
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()       
except Exception as e:
    logger.exception(e)
    raise e

try:
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()       
except Exception as e:
    logger.exception(e)
    raise e


