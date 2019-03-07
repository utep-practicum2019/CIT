import requests

from AccountManager.user import User


class UserManager:
    cit_url = "http://127.0.0.1:5000"
    database_path = "/api/v2/resources/database"
    database_url = cit_url + database_path

    @staticmethod
    def get_user(username):
        # Get info from database
        doc_data = {'collection_name': 'users', 'document_id': username}
        user = requests.get(UserManager.database_url, json=doc_data)
        if user.status_code == requests.codes.ok:
            user_js = user.json()
            return User(**user_js)
        return False

    @staticmethod
    def create_user(username, password, **kwargs):
        print("hello2")
        user_data = {'username': username, 'password': password, **kwargs}
        print(user_data)

        # user_data = json.dumps(user_data)
        doc_data = {'collection_name': 'users', 'document_id': username, 'document': user_data}

        # doc_data = json.dumps(doc_data)

        print(doc_data)

        r = requests.post(UserManager.database_url, json=doc_data)
        if r.status_code == requests.codes.ok:
            return True
        return False

    @staticmethod
    def update_user(username, updated_user):
        updated_user = User.to_dict(updated_user)
        doc_data = {'collection_name': 'users', 'document_id': username, 'document': {**updated_user}}
        r = requests.put(UserManager.database_url, json=doc_data)
        if r.status_code == requests.codes.ok:
            return True
        return False

    @staticmethod
    def delete_user(username):
        doc_data = {'collection_name': 'users', 'document_id': username}
        r = requests.delete(UserManager.database_url, json=doc_data)
        if r.status_code == requests.codes.ok:
            return True
        return False
