from hackbeta.constants import *
from hackbeta.utils.common import read_yaml,create_directories
from hackbeta.entity import (DataIngestionConfig,DataPreparationConfig)


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Create the root directory for artifacts as defined in the YAML configuration
        create_directories([self.config['artifacts_root']])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']

        # Ensure the data ingestion root directory exists
        create_directories([config['root_dir']])

        # Create a DataIngestionConfig object with paths from the YAML configuration
        data_ingestion_config = DataIngestionConfig(
            root_dir=config['root_dir'],
            source_file_path=config['source_file_path'],  # Path to the source CSV file
            local_data_file=config['local_data_file'],    # Target path for the moved CSV file
        )

        return data_ingestion_config
    
    def get_data_preparation_config(self) -> DataPreparationConfig:
        config =self.config.data_preparation

        create_directories([config.root_dir])

        data_preparation_config = DataPreparationConfig(
            root_dir=config['root_dir'],
            local_data_file=config['local_data_file'],
            
       
        )

        return data_preparation_config 
