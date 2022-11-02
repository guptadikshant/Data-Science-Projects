from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from sensor.entity.config_entitiy import DataValidationConfig
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils.main_utils import read_yaml_file
import pandas as pd
import sys


class DataValidation:

    def __init__(self, data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise SensorException(e, sys)

    def validate_number_of_columns(self, dataframe:pd.DataFrame) -> bool:
        try:
            number_of_columns = self._schema_config["columns"]
            if len(dataframe.columns) == number_of_columns:
                return True
            return False

        except Exception as e:
            raise SensorException(e, sys)

    def is_numerical_column_exist(self, dataframe:pd.DataFrame) -> bool:
        try:
            numerical_columns = self._schema_config["numerical_columns"]
            dataframe_columns = dataframe.columns
            numerical_columns_present = True
            missing_numerical_columns = []

            for num_cols in numerical_columns:
                if num_cols not in dataframe_columns:
                    numerical_columns_present = False
                    missing_numerical_columns.append(num_cols)
            logging.info(f"Missing numerical columns names : {missing_numerical_columns}")
            return numerical_columns_present

        except Exception as e:
            raise SensorException(e,sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise SensorException(e, sys)

    def detect_dataset_drift(self):
        pass

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            error_message = ""
            # Creating train and test file paths
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # Reading data from train and test file location
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # Validate number of columns
            train_status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not train_status:
                error_message = f"{error_message} Train dataframe does not contain all columns"
            test_status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not test_status:
                error_message = f"{error_message} Test dataframe does not contain all columns"

            # Validate numerical columns
            train_numerical_status = self.is_numerical_column_exist(dataframe=train_dataframe)
            if not train_numerical_status:
                error_message = f"{error_message} Train dataframe does not contain all numerical columns"
            test_numerical_status = self.is_numerical_column_exist(dataframe=test_dataframe)
            if not test_numerical_status:
                error_message = f"{error_message} Test dataframe does not contain all numerical columns"

            if len(error_message) > 0:
                raise SensorException(error_message, sys)

            # Lets check data drift
        except Exception as e:
            raise SensorException(e, sys)
