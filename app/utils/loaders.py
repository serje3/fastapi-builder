from typing import List, Dict

import yaml

from app.config import BUILDS_FILE_PATH, TASKS_FILE_PATH
from app.utils.abc.loader import AbstractLoader


class YamlLoader(AbstractLoader):
    def load_from_file(self, path: str):
        with open(path, "r") as file:
            parsed_yaml: dict = yaml.safe_load(file)
        return parsed_yaml


def get_loaded_builds() -> List[Dict]:
    print("Loading builds")
    parsed_yaml = YamlLoader().load_from_file(BUILDS_FILE_PATH)
    try:
        return parsed_yaml.get("builds")
    except KeyError:
        raise KeyError("Invalid key 'builds'. Maybe builds.yaml file is invalid")


def get_loaded_tasks() -> List[Dict]:
    print("Loading tasks")
    parsed_yaml = YamlLoader().load_from_file(TASKS_FILE_PATH)
    try:
        return parsed_yaml.get("tasks")
    except KeyError:
        raise KeyError("Invalid key 'tasks'. Maybe tasks.yaml file is invalid")
