from abc import ABC, abstractmethod
from typing import Any, List

from app.utils.exceptions import TooManyValuesError, DoesNotExist


class AbstractRepository(ABC):
    @abstractmethod
    def set(self, data):
        raise NotImplementedError

    @abstractmethod
    def get(self, reference):
        raise NotImplementedError

    @abstractmethod
    def all(self):
        raise NotImplementedError


class FakeRepository(AbstractRepository):
    _data: Any = {}

    def set(self, data):
        self._data = data

    def get(self, reference):
        raise NotImplementedError

    def all(self):
        return self._data


class ListRepository(FakeRepository):
    _data: List = []
    _search_key = "name"

    def __init__(self):
        if hasattr(self, "data"):
            self._data = self.data
        if hasattr(self, "search_key"):
            self._search_key = self.search_key

    def set(self, data):
        raise NotImplementedError

    def get(self, reference) -> Any:
        founded = self.filter(reference)
        # print(founded)
        if len(founded) > 1:
            raise TooManyValuesError()
        elif len(founded) == 0:
            raise DoesNotExist()
        return founded[0]

    def filter(self, reference) -> List:
        return list(filter(lambda row: row[self._search_key] == reference, self._data))

    def get_by_index(self, index) -> Any:
        return self._data[index]

    def size(self):
        return len(self._data)
