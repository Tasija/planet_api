import os
import json
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent.resolve()


def load_json_file(config_file_name):
    """
    :param config_file_name: name of configuration file
    :return: loaded json data as a dict
    """
    config_file_path = os.path.join(BASE_DIR, "configs", f"{config_file_name}")
    with open(config_file_path) as config_file:
        data = json.load(config_file)
    return data