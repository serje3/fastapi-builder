from typing import List

from app.repositories.builds import BuildsRepository
from app.schemas import Build
from app.utils.abc.service import AbstractService


class BuildsService(AbstractService):
    repository: BuildsRepository

    def get_tasks_by_build_name(self, name: str) -> List[str]:
        return self.get_build_by_name(name).tasks

    def get_build_by_name(self, name) -> Build:
        return self.repository.get(name)
