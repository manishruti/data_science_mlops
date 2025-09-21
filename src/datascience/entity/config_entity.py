from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_url:str
    local_data_file:Path
    unzip_dir:Path


@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:Path
    local_data_file:Path
    all_schema:dict


@dataclass
class DataTransformationConfig:
    root_dir:Path
    data_file_path:Path

@dataclass
class ModelTrainerConfig:
    root_dir:Path
    train_file_path:Path
    test_file_path:Path
    model_name:str
    penalty: str
    l1_ratio: float
    target_column:str


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_file_path: Path
    model_path: Path
    metric_file_name: Path
    all_params: dict
    target_column: str
    mlflow_uri: str
