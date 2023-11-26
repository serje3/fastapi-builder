from typing import List, TypeAlias, Optional

from pydantic import BaseModel

TaskDependencies: TypeAlias = List[str]


class Task(BaseModel):
    name: str
    dependencies: Optional[TaskDependencies] = []


class TaskRequestBody:
    class GetTasksByBuild(BaseModel):
        build: str
