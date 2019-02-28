from group import Group
import requests
 
class GroupManager:
    cit_url = "http://127.0.0.1:5000"
    groups_path = "/api/v2/database/groups"
    groups_url = cit_url + groups_path

    @staticmethod
    def get_group(group_id):
        group = requests.get(GroupManager.groups_url + '/' + group_id)
        group_js = group.json()
        return Group(**group_js)

    @staticmethod
    def get_groups():
        groups = requests.get(GroupManager.groups_url)
        groups_js = groups.json()
        return groups_js

    @staticmethod
    def create_group(group_id, **kwargs):
        # TODO: test group creation
        # Check if group already exists
        if GroupManager.get_group(group_id)is None:
            group_data = {'group_id': group_id, **kwargs}
            r = requests.post(GroupManager.groups_url + '/' + group_id, json=group_data)
            if r.status_code == requests.codes.ok:
                return Group(group_id, **kwargs)
        # group_id is already used or request failed
        return None

    @staticmethod
    def delete_group(group_id):
        return None

    @staticmethod
    def add_user(group_id, username):
        return None

    @staticmethod
    def remove_user(group_id, username):
        return None

    @staticmethod
    def add_platform(group_id, platform):
        return None

    @staticmethod
    def remove_platform(group_id, platform):
        return None

    @staticmethod
    def add_chat(group_id, chat_id):
        return None

    @staticmethod
    def remove_chat(group_id):
        return None
