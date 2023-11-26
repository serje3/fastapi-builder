from app.repositories import TasksRepository, BuildsRepository
from app.services import BuildsService, TasksService


def get_tasks_service():
    return TasksService(TasksRepository())


def get_builds_service():
    return BuildsService(BuildsRepository())
