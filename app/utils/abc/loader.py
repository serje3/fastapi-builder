from abc import ABC, abstractmethod


class AbstractLoader(ABC):
    @abstractmethod
    def load_from_file(self, path: str):
        pass
