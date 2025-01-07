from ProjectApi import ProjectApi


api = ProjectApi("https://ru.yougile.com/api-v2")
auth_token = ""


def test_create_project():
    title = "HomeWork8"
    result = api.create_project(title, auth_token)
    assert result.status_code == 201


def test_create_project_negative():
    auth_token_negative = ""
    title = "HomeWork8"
    result = api.create_project(title, auth_token_negative)
    assert result.status_code == 401


def test_get_projects():
    resp = api.get_project(auth_token)
    assert resp.status_code == 200, \
        f"Test failed: Status code was {resp.status_code}"


def test_get_projects_negative():
    auth_token = ""
    resp = api.get_project(auth_token)
    assert resp.status_code == 401, \
        f"Test failed: Status code was {resp.status_code}"


def test_edit_project():
    title = "HomeWork8"
    project_id = api.create_project_to_get_id(title, auth_token)
    print(f"Project created with ID: {project_id}")
    new_title = "Новый"
    deleted = False
    edit_response = api.edit_project(
        project_id, deleted, new_title, auth_token)
    print("Project updated:", edit_response)


def test_edit_project_negative():
    title = "HomeWork8"
    project_id = api.create_project_to_get_id(title, auth_token)
    print(f"Project created with ID: {project_id}")
    new_title = "Новый"
    deleted = False
    invalid_project_id = 999999
    edit_response = api.edit_project(
        invalid_project_id, deleted, new_title, auth_token)
    assert edit_response.status_code == 404


def test_get_project_by_id():
    title = "HomeWork8_get_project_by_id"
    project_id = api.create_project_to_get_id(title, auth_token)
    print(f"Project created with ID: {project_id}")
    get_response = api.get_project_by_id(project_id, auth_token)
    assert get_response.status_code == 200


def test_get_project_by_id_negative():
    title = "HomeWork8_get_project_by_id"
    project_id = api.create_project_to_get_id(title, auth_token)
    print(f"Project created with ID: {project_id}")
    invalid_project_id = 999999
    get_response = api.get_project_by_id(invalid_project_id, auth_token)
    assert get_response.status_code == 404
