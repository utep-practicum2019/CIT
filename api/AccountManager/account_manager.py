from AccountManager.group_manager import GroupManager


class AccountManager:
    @staticmethod
    def update_user(username, updated_user):
        return GroupManager.update_user(username, updated_user)

    @staticmethod
    def delete_user(username):
        return GroupManager.delete_user(username)

    @staticmethod
    def create_groups(group_count=0, users_per_group=0, filepath=None):
        return GroupManager.create_groups(group_count, users_per_group, filepath)

    @staticmethod
    def update_group(group_id, updated_group):
        return GroupManager.update_group(group_id, updated_group)

    @staticmethod
    def delete_group(group_id):
        return GroupManager.delete_group(group_id)

    @staticmethod
    def attach_platform(group_id, platform_name):
        return GroupManager.attach_platform(group_id, platform_name)

    @staticmethod
    def detach_platform(platform_name):
        return GroupManager.detach_platform(platform_name)
