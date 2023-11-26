from abc import ABC

from app.utils.abc.repository import AbstractRepository


class AbstractService(ABC):
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository
