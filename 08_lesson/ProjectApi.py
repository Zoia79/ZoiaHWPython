import requests


class ProjectApi:
    def __init__(self, url):
        self.url = url

    def create_project(self, title, auth_token):
        headers = {'Authorization': f'Bearer {auth_token}',
                   'Content-Type': 'application/json'}
        project = {"title": title}
        resp = requests.post(
            self.url + '/projects', headers=headers, json=project)
        return resp

    def get_project(self, auth_token):
        headers = {'Authorization': f'Bearer {auth_token}',
                   'Content-Type': 'application/json'}
        resp = requests.get(self.url + '/projects', headers=headers)
        return resp

    def create_project_to_get_id(self, title, auth_token):
        headers = {'Authorization': f'Bearer {auth_token}',
                   'Content-Type': 'application/json'}
        project = {"title": title}
        resp = requests.post(self.url + '/projects',
                             headers=headers, json=project)
        project_data = resp.json()
        return project_data.get('id')

    def edit_project(self, project_id, deleted, new_title, auth_token):
        headers = {'Authorization': f'Bearer {auth_token}',
                   'Content-Type': 'application/json'}
        project = {"deleted": deleted, "title": new_title}
        resp = requests.put(f'{self.url}/projects/{project_id}',
                            headers=headers, json=project)
        return resp

    def get_project_by_id(self, project_id, auth_token):
        headers = {'Authorization': f'Bearer {auth_token}',
                   'Content-Type': 'application/json'}
        resp = requests.get(f'{self.url}/projects/{project_id}',
                            headers=headers)
        return resp
