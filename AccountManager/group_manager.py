from group import Group
import requests

# TODO: check where the request will be made groupsWJson or groups/id

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
                return True
        # group_id is already used or request failed
        return False

    @staticmethod
    def delete_group(group_id):
        # TODO: test group deletion
        r = requests.delete(GroupManager.groups_url + '/' + group_id)
        if r.status_code == requests.codes.ok:
            return True
        return False

    @staticmethod
    def add_user(group_id, username):
        # TODO: test user addition
        group_data = {'group_id':group_id, 'users':username}
        r = requests.post(GroupManager.groups_url + '/' + group_id, json=group_data)
        if r.status_code == requests.codes.ok:
            return True
        return False

    @staticmethod
    def remove_user(group_id, username):
        # TODO: test user removal
        group_data = {'group_id':group_id, 'username':username}
        # TODO:  what does the URL look for user deletion from group?
        r = requests.delete(GroupManager.groups_url + '/' + group_id, json=group_data)
        if r.status_code == requests.codes.ok:
            return True
        return False

    @staticmethod
    def add_platform(group_id, platform):
        # TODO: test platform addition
        group_data = {'group_id':group_id, 'platforms':platform}
        r = requests.put(GroupManager.groups_url + '/' + group_id, json=group_data)
        if r.status_code == requests.codes.ok:
            return True
        return False

    @staticmethod
    def remove_platform(group_id, platform):
        # TODO: test platform removal
        group_data = {'group_id':group_id, 'platforms':platform}
        r = requests.delete(GroupManager.groups_url + '/' + group_id, json=group_data)
        if r.status_code == requests.codes.ok:
            return True
        return False

    @staticmethod
    def add_chat(group_id, chat_id):
        # TODO: test chat addition
        group_data = {'group_id':group_id, 'chat_id':chat_id}
        r = requests.put(GroupManager.groups_url + '/' + group_id, json=group_data)
        if r.status_code == requests.codes.ok:
            return True
        return False

    @staticmethod
    def remove_chat(group_id):
        # TODO: test chat removal
        group_data = {'group_id':group_id, 'chat_id':None}
        r = requests.out(GroupManager.groups_url + '/' + group_id, json=group_data)
        if r.status_code == requests.codes.ok:
            return True
        return False
