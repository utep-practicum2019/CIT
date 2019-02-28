from user import User
import requests

class UserManager:
    cit_url = "http://127.0.0.1:5000"
    users_path = "/api/v2/database/users"
    users_url = cit_url + users_path

    @staticmethod
    def get_user(username):
        # Get info from database
        user = requests.get(UserManager.users_url + '/' + username)
        user_js = user.json()
        return User(**user_js)

    @staticmethod
    def get_users():
        users = requests.get(UserManager.users_url)
        users_js = users.json()
        return users_js

    @staticmethod
    def create_user(username, password, **kwargs):
        # TODO: test user creation
        # check if user exists
        if UserManager.get_user(username) is None:
            user_data = {'username':username, 'password':password, **kwargs}
            r = requests.post(UserManager.users_url + '/' + username, json=user_data)
            if r.status_code == requests.codes.ok:
                return User(username, password, **kwargs)
        # user already exists or request failed
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
