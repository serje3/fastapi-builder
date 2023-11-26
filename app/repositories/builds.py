from typing import List

from app.schemas import Build
from app.utils.abc.repository import ListRepository
from app.utils.exceptions import BuildDoesNotExist, DoesNotExist, TooManyValuesError, BuildTooManyValuesError
from app.utils.loaders import get_loaded_builds


class BuildsRepository(ListRepository):
    data: List[Build] = get_loaded_builds()
    search_key = "name"

    def get(self, name) -> Build:
        try:
            return Build(**super().get(name))
        except DoesNotExist:
            raise BuildDoesNotExist(name)
        except TooManyValuesError:
            raise BuildTooManyValuesError(name)
