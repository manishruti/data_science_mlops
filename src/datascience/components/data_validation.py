## DataValidation Components
import os
import pandas as pd
from urllib import request
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.local_data_file)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()
            report_lines = []

            for col in all_cols:
                if col not in all_schema:
                    validation_status=False
                    report_lines.append(f"Column:{col}, {validation_status}")
                else:
                    validation_status=True
                    report_lines.append(f"Column:{col}, {validation_status}")

            # Write all results at once
            with open(self.config.STATUS_FILE, 'w') as f:
                for line in report_lines:
                    f.write(line + '\n')

            logger.info(f"Validation status: {validation_status}")
            return validation_status

        except Exception as e:
            logger.exception(e)
            raise e