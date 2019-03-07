import requests

from AccountManager.group import Group


class GroupManager:
    cit_url = "http://127.0.0.1:5000"
    database_path = "/api/v2/resources/database"
    database_url = cit_url + database_path

    @staticmethod
    def get_group(group_id):
        doc_data = {'collection_name': 'groups', 'document_id': group_id}
        print(doc_data)
        r = requests.get(GroupManager.database_url, json=doc_data)
        print(r)
        if r.status_code == requests.codes.ok:
            group_js = r.json()
            return Group(**group_js)
        return None

    @staticmethod
    def create_group(group_id, **kwargs):
        # Check if group already exists
        if GroupManager.get_group(group_id) is None:
            group_data = {'collection_name': "groups", 'document_id': group_id, **kwargs}
            print(group_data)
            r = requests.post(GroupManager.database_url, json=group_data)
            if r.status_code == requests.codes.ok:
                return True
        # group_id is already used or request failed
        return False

    @staticmethod
    def update_group(group_id, updated_group):
        group_data = {'group_id': group_id, 'updated_group': {**updated_group}}
        r = requests.put(GroupManager.database_url, json=group_data)
        if r.status_code == requests.codes.ok:
            return True
        return False

    @staticmethod
    def delete_group(group_id):
        r = requests.delete(GroupManager.database_url)
        if r.status_code == requests.codes.ok:
            return True
        return False
