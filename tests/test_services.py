from typing import List

from app.schemas import Build
from app.utils.exceptions import BuildDoesNotExist, BuildTooManyValuesError
from tests.conftest import get_test_builds_service, get_test_tasks_service

builds_service = get_test_builds_service()
tasks_service = get_test_tasks_service()

tasks_forward_interest = [
    'build_teal_leprechauns',
    'coloring_aqua_centaurs',
    'coloring_navy_golems',
    'enable_lime_leprechauns',
    'enable_lime_leprechauns',
    'enable_olive_humans',
    'enable_silver_humans',
    'write_blue_ogres',
    'write_fuchsia_golems'
]

tasks_front_arm = [
    'build_lime_golems',
    'coloring_black_goblins',
    'design_maroon_witches',
    'design_teal_golems',
    'design_yellow_centaurs',
    'map_purple_humans',
    'read_aqua_orcs',
    'read_gray_golems',
    'train_white_leprechauns',
    'upgrade_gray_humans'
]


def test_builds_service__get_build_by_name():
    build_forward_interest: Build = builds_service.get_build_by_name("forward_interest")
    for i in range(len(build_forward_interest.tasks)):
        assert tasks_forward_interest[i] == build_forward_interest.tasks[i]

    build_front_arm: Build = builds_service.get_build_by_name("front_arm")

    for i in range(len(build_front_arm.tasks)):
        assert tasks_front_arm[i] == build_front_arm.tasks[i]

    try:
        not_existed_build: Build = builds_service.get_build_by_name(
            "blablalblsdsakdknasjkdhsajdfasda_tochno_ne_sushestvuet")
    except Exception as e:
        assert isinstance(e, BuildDoesNotExist)

    try:
        too_many_builds: Build = builds_service.get_build_by_name("duplicated_build")
    except Exception as e:
        assert isinstance(e, BuildTooManyValuesError)


def test_builds_service__get_tasks_by_build_name():
    tasks: List[str] = builds_service.get_tasks_by_build_name("forward_interest")
    for i in range(len(tasks)):
        assert tasks[i] == tasks_forward_interest[i]


design_teal_golems_dependencies = [
    'write_teal_golems',
    'write_white_golems',
    'coloring_silver_golems',
    'enable_white_golems',
    'train_maroon_golems',
]

enable_blue_goblins_dependencies = [
    'create_gray_goblins'
]


def test_tasks_service__get_task_dependencies():
    dependencies: List[str] = tasks_service.get_task_dependencies("design_teal_golems")
    for i in range(len(design_teal_golems_dependencies)):
        assert dependencies[i] == design_teal_golems_dependencies[i]


def test_tasks_service__get_tasks_with_dependencies():
    design_teal_golems_task_with_dependencies = design_teal_golems_dependencies + ['design_teal_golems']
    enable_blue_goblins_task_with_dependencies = enable_blue_goblins_dependencies + ['enable_blue_goblins']
    right_answer = design_teal_golems_task_with_dependencies + enable_blue_goblins_task_with_dependencies

    test_result = tasks_service.get_tasks_with_dependencies(["design_teal_golems", "enable_blue_goblins"])

    assert len(test_result) == len(right_answer)

    for i in range(len(right_answer)):
        assert test_result[i] == right_answer[i]