from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_file_path: Path
    local_data_file: Path


@dataclass(frozen=True)
class DataPreparationConfig:
    root_dir: Path
    local_data_file: Path