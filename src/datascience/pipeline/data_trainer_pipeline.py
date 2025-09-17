from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer



STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def initiate_model_trainer(self):
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train_model()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.info(e)
            raise e
