from user_manager import UserManager
from group import Group
from group_manager import GroupManager

class AccountManager:
    @staticmethod
    def get_user(username):
        return UserManager.get_user(username)

    @staticmethod
    def create_user(username, password):
        pass

    @staticmethod
    def update_user(username, updated_user):
        return UserManager.update_user(username, updated_user)

    @staticmethod
    def delete_user(username):
        return UserManager.delete_user(username)

    @staticmethod
    def get_group(group_id):
        return GroupManager.get_group(group_id)

    @staticmethod
    def create_group(group_id, **kwargs):
        return GroupManager.create_group(group_id, **kwargs)

    @staticmethod
    def create_groups(group_count, users_per_group, filepath=None):
        if filepath is not None:
            return False

        try:
            freader = open('next_group_id', 'r')
            freader.close()
        except FileNotFoundError:
            fwriter = open('next_group_id', 'w')
            fwriter.write('1')
            fwriter.close()

        for i in range(group_count):
            freader = open('next_group_id', 'r')
            group_id = int(freader.readline())
            freader.close()

            group = Group(group_id)
            for j in range(users_per_group):
                # TODO: call to Connections
                username = 'user' + str(j) + "G" + str(group_id)
                password = "pass1"
                r_ip = "127.0.0.1" + str(i) + str(j)

                group.members.append(username)
                if not UserManager.create_user(username, password, remote_ip=r_ip):
                    return False
            if not GroupManager.create_group(group.group_id, members=group.members):
                return False
            fwriter = open('next_group_id', 'w')
            fwriter.write(str(group_id + 1))
            fwriter.close()
        return True

    @staticmethod
    def update_group(group_id, updated_group):
        return GroupManager.update_group(group_id, updated_group)

    @staticmethod
    def delete_group(group_id):
        return GroupManager.delete_group(group_id)
