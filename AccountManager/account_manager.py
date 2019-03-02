from user_manager import UserManager
from group_manager import GroupManager

class AccountManager:
    @staticmethod
    def get_user(username):
        return UserManager.get_user(username)

    @staticmethod
    def get_users():
        return UserManager.get_users()

    @staticmethod
    def create_user(username, password, **kwargs):
        return UserManager.create_user(username, password, **kwargs)

    @staticmethod
    def delete_user(username):
        return UserManager.delete_user(username)

    @staticmethod
    def set_group(username, group_id):
        return UserManager.set_group(username, group_id)

    @staticmethod
    def remove_group(username):
        return UserManager.remove_group(username)

    @staticmethod
    def set_internal_ip(username, internal_ip):
        return UserManager.set_internal_ip(username, internal_ip)

    @staticmethod
    def remove_internal_ip(username):
        return UserManager.remove_internal_ip(username)

    @staticmethod
    def get_group(group_id):
        return GroupManager.get_group(group_id)

    @staticmethod
    def get_groups():
        return GroupManager.get_groups()

    @staticmethod
    def create_group(group_id, **kwargs):
        return GroupManager.create_group(group_id, **kwargs)

    @staticmethod
    def delete_group(group_id):
        return GroupManager.delete_group(group_id)

    @staticmethod
    def add_user(group_id, username):
        return GroupManager.add_user(group_id, username)

    @staticmethod
    def remove_user(group_id, username):
        return GroupManager.remove_user(group_id, username)

    @staticmethod
    def add_platform(group_id, platform):
        return GroupManager.add_platform(platform)

    @staticmethod
    def remove_platform(group_id, platform):
        return GroupManager.remove_platform(group_id, platform)

    @staticmethod
    def add_chat(group_id, chat_id):
        return GroupManager.add_chat(group_id, chat_id)

    @staticmethod
    def remove_chat(group_id):
        return GroupManager.remove_chat(group_id)
