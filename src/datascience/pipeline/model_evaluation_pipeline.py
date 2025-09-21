from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger


STAGE_NAME = "Data Ingestion stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_validation(self):
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  
        except Exception as e:
            raise e
            logger.exception(e)
        