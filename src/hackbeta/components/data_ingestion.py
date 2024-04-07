import os
import shutil
import urllib.request as request
import zipfile
from hackbeta.logging import logger
from hackbeta.utils.common import get_size
from hackbeta.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config):
        self.config = config

    def move_csv_file(self):
        """
        Moves the CSV file from a source location to the target location
        specified in the configuration. If the file already exists at the target
        location, the function logs a message and does not overwrite the file.
        """
        source_file_path = Path(self.config.source_file_path)  # Path to the source CSV file
        target_file_path = Path(self.config.local_data_file)  # Target location as per configuration

        # Ensure the target directory exists
        target_file_path.parent.mkdir(parents=True, exist_ok=True)

        if not source_file_path.exists():
            logger.error(f"Source CSV file does not exist at {source_file_path}")
            return

        if target_file_path.exists():
            logger.info(f"File already exists at target location: {target_file_path}")
            return

        try:
            shutil.move(str(source_file_path), str(target_file_path))
            logger.info(f"CSV file moved successfully from {source_file_path} to {target_file_path}")
        except Exception as e:
            logger.error(f"Failed to move CSV file: {e}")
