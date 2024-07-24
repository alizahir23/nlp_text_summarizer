import os
from box.exceptions import BoxValueError
import yaml
from nlp_text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return its contents as a ConfigBox.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Raises:
        ValueError: If yaml file is empty
        e: empty file

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): A list of directory paths.
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory: {path} created successfully")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size of a file in KB

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in KB
    """
    size = os.path.getsize(path)
    return f"{size / 1024:.2f} KB"
