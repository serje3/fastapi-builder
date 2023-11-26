from typing import List

from conftest import client
from test_services import design_teal_golems_dependencies, enable_blue_goblins_dependencies


def test_get_tasks_by_build_ok():
    response = client.post("/tasks/get_by_build", json={
        'build': 'test_build'
    })
    right_answer = design_teal_golems_dependencies + ['design_teal_golems'] + \
                   enable_blue_goblins_dependencies + ['enable_blue_goblins']
    json: List[str] = response.json()
    assert type(json) == list
    assert response.status_code == 200
    assert len(json) == len(right_answer)
    for i in range(len(right_answer)):
        assert json[i] == right_answer[i]


def test_get_tasks_by_build_does_not_exist():
    response = client.post("/tasks/get_by_build", json={
        'build': 'test_build_NOT_EXISTING_BLABLABLABLALBALLAB'
    })

    assert response.status_code == 400
    assert response.json() == {
        'detail': "Build named 'test_build_NOT_EXISTING_BLABLABLABLALBALLAB' does not exist"
    }

    response = client.post("/tasks/get_by_build", json={
        'build': 'test_build_with_not_existing_task'
    })

    assert response.status_code == 400
    assert response.json() == {
        'detail': "Task named 'this_task_does_not_exist' does not exist"
    }


def test_get_tasks_by_build_too_many_values_error():
    response = client.post("/tasks/get_by_build", json={
        'build': 'test_build_too_many_values'
    })

    assert response.status_code == 400
    assert response.json() == {
        'detail': "Build named 'test_build_too_many_values' found more than one"
    }

    response = client.post("/tasks/get_by_build", json={
        'build': 'test_build_task_too_many_values'
    })

    assert response.status_code == 400
    assert response.json() == {
        'detail': "Task named 'this_task_duplicated' found more than one"
    }
