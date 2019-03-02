from user import User
import requests

class UserManager:
    cit_url = "http://127.0.0.1:5000"
    database_path = "/api/v2/database/"
    database_url = cit_url + database_path

    @staticmethod
    def get_user(username):
        # Get info from database
        user_data = {'username':username}
        user = requests.get(UserManager.database_url, json=user_data)
        user_js = user.json()
        return User(**user_js)

    @staticmethod
    def get_users():
        users = requests.get(UserManager.database_url)
        users_js = users.json()
        return users_js

    @staticmethod
    def create_user(username=None, **kwargs):
        # TODO: test user creation
        if username is None:
            # TODO: generate random username
            username = 'user'

        # check if user exists
        if UserManager.get_user(username) is None:
            user = User(username, **kwargs)
            r = requests.post(UserManager.database_url, data=user.toJSON())
            if r.status_code != requests.codes.ok:
                return False
            # TODO: make request to connection manager for password
            return True
        # user already exists or get failed
        return False
    
    @staticmethod
    def delete_user(username):
        # TODO: test user deletion
        user_data = {'username':username}
        r = requests.delete(UserManager.database_url, json=user_data)
        if r.status_code == requests.codes.ok:
            return True
        return False
    
    @staticmethod
    def update_user(username, updated_user):
        # TODO: test group association
        user_data = {'username':username, 'updated_user':{**updated_user}}
        r = requests.put(UserManager.database_url, json=user_data)
        if r.status_code == requests.codes.ok:
            return True
        return False
