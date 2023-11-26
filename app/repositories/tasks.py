from typing import List

from app.schemas import Task
from app.utils.abc.repository import ListRepository
from app.utils.exceptions import DoesNotExist, TaskDoesNotExist, TooManyValuesError, TaskTooManyValuesError
from app.utils.loaders import get_loaded_tasks


class TasksRepository(ListRepository):
    data: List[Task] = get_loaded_tasks()
    search_key = "name"

    def get(self, name) -> Task:
        try:
            return Task(**super().get(name))
        except DoesNotExist:
            raise TaskDoesNotExist(name)
        except TooManyValuesError:
            raise TaskTooManyValuesError(name)
