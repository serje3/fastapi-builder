from typing import List, Optional

from pydantic import BaseModel


class Build(BaseModel):
    name: str
    tasks: Optional[List[str]] = []
