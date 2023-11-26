from typing import List, Annotated

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from app.dependencies import get_tasks_service, get_builds_service
from app.schemas.tasks import TaskRequestBody
from app.services import BuildsService, TasksService
from app.utils.exceptions import BuildDoesNotExist, BuildTooManyValuesError, TaskDoesNotExist, \
    TaskTooManyValuesError

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/get_by_build", response_model=List[str])
def get_tasks_by_build(body: TaskRequestBody.GetTasksByBuild,
                       task_service: Annotated[TasksService, Depends(get_tasks_service)],
                       builds_service: Annotated[BuildsService, Depends(get_builds_service)]):
    try:
        build_task_names: List[str] = builds_service.get_tasks_by_build_name(body.build)
    except (BuildDoesNotExist, BuildTooManyValuesError) as e:
        raise HTTPException(400, e.get_message())

    try:
        tasks: List[str] = task_service.get_tasks_with_dependencies(build_task_names)
    except (TaskDoesNotExist, TaskTooManyValuesError) as e:
        raise HTTPException(400, e.get_message())

    return tasks
