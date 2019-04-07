import re

import requests

from AccountManager.group import Group
from AccountManager.user_manager import UserManager, get_user, create_user

cit_url = 'http://127.0.0.1:5001'
database_path = '/api/v2/resources/database'
database_url = cit_url + database_path
connection_path = '/api/v2/resources/connection'
connection_url = cit_url + connection_path
# TODO: set to an absolute path
id_filepath = 'next_group_id.txt'


def get_group(group_id):
    # put data in the correct format
    doc_data = {
        'collection_name': 'groups',
        'document_id': group_id
    }
    # retrieve info from database
    r = requests.get(database_url, json=doc_data)
    if r.status_code == requests.codes.ok:
        group_js = r.json()
        return Group(**group_js)
    return None


def create_group(group_id, users, **kwargs):
    # Check if group already exists
    if get_group(group_id) is not None:
        # group_id is already used or request failed
        return False

    # create group and add members
    group = Group(group_id)
    for user in users:
        group.members.append(user["username"])
        print(user["username"])
        if not create_user(user['username'], user['password'], remote_ip=user['pptpIP'], group_id=group_id):
            return False

    # put data in the correct format
    doc_data = {
        'collection_name': 'groups',
        'document_id': group_id,
        'document': {
            'group_id': group_id,
            'members': group.members,
            **kwargs
        }
    }
    # store in the database
    r = requests.post(database_url, json=doc_data)
    if r.status_code == requests.codes.ok:
        return True
    return False


def verify_file(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return False
    lines = [line for line in lines if re.match('.*\\S.*', line)]
    if not lines:
        # empty file
        return False

    file_users = []
    for line in lines:
        users = line.strip().split()
        for user in users:
            if get_user(user) is not None:
                # username is taken
                return False
            if user in file_users:
                # duplicate user
                return False
            file_users.append(user)
    return True


def set_next_id(next_id):
    with open(id_filepath, 'w') as f:
        f.write(str(next_id))


def get_next_id():
    try:
        with open(id_filepath, 'r') as f:
            next_id = int(f.readline())
        while get_group(next_id) is not None:
            next_id += 1
        return next_id
    except (FileNotFoundError, ValueError):
        # recover latest group_id
        next_id = 1
        while get_group(next_id) is not None:
            next_id += 1
        set_next_id(next_id + 1)
        return next_id


def create_with_file(filepath):
    if not verify_file(filepath):
        return False

    with open(filepath, 'r') as f:
        lines = f.readlines()
    for line in lines:
        group_id = get_next_id()

        users = line.rstrip().split()
        # get [username,password,remote_ip] from connections
        r = requests.post(connection_url, json={'usernames': users})
        if r.status_code != requests.codes.ok:
            return False
        # unpack data
        json_data = r.json()
        users = [json_data[k] for k in json_data.keys()]
        # create and store group
        if not create_group(group_id, users):
            return False

        set_next_id(str(group_id + 1))
    return True


def create_with_count(group_count, users_per_group):
    # create i groups with j users
    for i in range(group_count):
        group_id = get_next_id()

        # get [username,password,remote_ip] from connections
        r = requests.post(connection_url, json={'num_users': users_per_group})
        if r.status_code != requests.codes.ok:
            return False
        # unpack data
        json_data = r.json()
        json_data = json_data["usersDictionary"]
        users = [json_data[k] for k in json_data.keys()]
        # create and store group
        if not create_group(group_id, users):
            return False

        set_next_id(str(group_id + 1))
    return True


def remove_user(username, group_id):
    current = get_group(group_id)
    if current is not None and username in current.members:
        new = Group(group_id, members=current.members)
        new.members.remove(username)
        GroupManager.update_group(new.group_id, new)


class GroupManager:
    @staticmethod
    def update_user(username, update_user):
        current = get_user(username)
        if current is None:
            return False
        if current.group_id is not None \
                and update_user.group_id is not None \
                and current.group_id != update_user.group_id:
            remove_user(username, current.group_id)
        return UserManager.update_user(username, update_user)

    @staticmethod
    def delete_user(username):
        current = get_user(username)
        if current is not None:
            result = UserManager.delete_user(username)
        if result and current.group_id is not None:
            remove_user(username, current.group_id)
        return result

    @staticmethod
    def create_groups(group_count=0, users_per_group=0, filepath=None):
        if filepath is not None:
            return create_with_file(filepath)
        if group_count > 0 and users_per_group > 0:
            return create_with_count(group_count, users_per_group)
        return False

    @staticmethod
    def update_group(group_id, updated_group):
        current = get_group(group_id)
        if current is None:
            # group does not exist
            return False

        if group_id != updated_group.group_id:
            # can't change group_id
            return False

        # put data in the correct format
        group_data = {
            'collection_name': 'groups',
            'document_id': group_id,
            'document': {
                **updated_group.to_dict()
            }
        }
        # store group in the database
        r = requests.put(database_url, json=group_data)
        if r.status_code == requests.codes.ok:
            return True
        return False

    @staticmethod
    def delete_group(group_id):
        current = get_group(group_id)
        if current is None:
            # group does not exist
            return False

        # delete group members
        for user in current.members:
            if not UserManager.delete_user(user):
                return False

        # TODO: do I need to delete related platforms as well?
        # maybe at least chat needs to know

        # put data in the correct format
        doc_data = {
            'collection_name': 'groups',
            'document_id': group_id
        }
        # delete from database
        r = requests.delete(database_url, json=doc_data)
        if r.status_code != requests.codes.ok:
            return False

        if group_id < get_next_id():
            set_next_id(group_id)
        return True

    @staticmethod
    def attach_platform(group_id, platform_id):
        current = get_group(group_id)
        if current is None:
            return False
        if platform_id in current.platforms:
            return False

        # updated_group = Group(group_id, platforms=current.platforms)
        current.platforms.append(platform_id)
        return GroupManager.update_group(group_id, current)

    @staticmethod
    def detach_platform(group_id, platform_id):
        current = get_group(group_id)
        if current is None:
            return False
        if platform_id not in current.platforms:
            return False
        # updated_group = Group(group_id, platforms=current.platforms)
        current.platforms.remove(platform_id)
        return GroupManager.update_group(group_id, current)
