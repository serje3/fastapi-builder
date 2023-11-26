from typing import List, Dict

from fastapi.testclient import TestClient

from app.config import BASE_DIR
from app.dependencies import get_tasks_service, get_builds_service
from app.main import app
from app.repositories import BuildsRepository, TasksRepository
from app.services import BuildsService, TasksService
from app.utils.loaders import YamlLoader

client = TestClient(app)


def get_test_loaded_builds() -> List[Dict]:
    print("Loading test builds")
    parsed_yaml = YamlLoader().load_from_file(BASE_DIR.parent / "tests/builds/builds.yaml")
    try:
        return parsed_yaml.get("builds")
    except KeyError:
        raise KeyError("Invalid key 'builds'. Maybe builds.yaml file is invalid")


def get_test_loaded_tasks() -> List[Dict]:
    print("Loading test tasks")
    parsed_yaml = YamlLoader().load_from_file(BASE_DIR.parent / "tests/builds/tasks.yaml")
    try:
        return parsed_yaml.get("tasks")
    except KeyError:
        raise KeyError("Invalid key 'tasks'. Maybe tasks.yaml file is invalid")


class BuildsTestRepository(BuildsRepository):
    data = get_test_loaded_builds()


class TasksTestRepository(TasksRepository):
    data = get_test_loaded_tasks()


def get_test_builds_service():
    return BuildsService(BuildsTestRepository())


def get_test_tasks_service():
    return TasksService(TasksTestRepository())


app.dependency_overrides[get_tasks_service] = get_test_tasks_service
app.dependency_overrides[get_builds_service] = get_test_builds_service
