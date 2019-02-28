from user import User
import requests

class UserManager:

    user_url = "citsystem.com/api/v2/user"

    @staticmethod
    def get_user(username):
        r = requests.get(user)
        # TODO: get info from database
        data = {'username':'user1', 'password':'pass1'}

        if data is None:
            # user does not exist
            return None
        assert data['username'] == username
        return User(**data)

    @staticmethod
    def get_users():
        # TODO: get info from database
        return None

    @staticmethod
    def create_user(username, password, **kwargs):
        # check if user exists
        if get_user(username) is None:
            # TODO: store in  database
            return User(username, password, **kwargs)
        # user already exists
        return None
    
    @staticmethod
    def delete_user(username):
        return None
    
    @staticmethod
    def set_group(username, group_id):
        return None

    @staticmethod
    def remove_group(username):
        return None

    @staticmethod
    def set_internal_ip(username, internal_ip):
        return None

    @staticmethod
    def remove_internal_ip(username):
        return None
