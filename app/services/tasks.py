from typing import List

from app.repositories.tasks import TasksRepository
from app.schemas import Task
from app.utils.abc.service import AbstractService


class TasksService(AbstractService):
    repository: TasksRepository

    def get_tasks_with_dependencies(self, task_names: List[str]) -> List[str]:
        return [name_nested for name in task_names for name_nested in [*self.get_task_dependencies(name), name]]

    def get_task_dependencies(self, task_name: str) -> List[str]:
        task: Task = self.repository.get(task_name)
        dependencies = []
        for name in task.dependencies:
            dependencies.extend([*self.get_task_dependencies(name), name])

        return dependencies
