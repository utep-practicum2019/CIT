import requests
from AccountManager.user import User


cit_url = 'http://127.0.0.1:5001'
database_path = '/api/v2/resources/database'
database_url = cit_url + database_path
connection_path = '/api/v2/resources/connection'
connection_url = cit_url + connection_path


def get_user(username):
    # Get info from database
    doc_data = {
        'collection_name': 'users',
        'document_id': username
    }
    r = requests.get(database_url, json=doc_data)
    if r.status_code == requests.codes.ok:
        user_js = r.json()
        return User(**user_js)
    return None


def create_user(username, password, **kwargs):
    # username/password/remote_ip should already come from connection subsystem
    if get_user(username) is not None:
        # username is already taken
        return False

    # put the data in the correct format
    user_data = {
        'username': username,
        'password': password,
        **kwargs
    }
    if 'note' not in kwargs:
        user_data['note'] = ""
    if 'alias' not in kwargs:
        user_data['alias'] = ""
    doc_data = {
        'collection_name': 'users',
        'document_id': username,
        'document': user_data
    }
    # store in the database
    r = requests.post(database_url, json=doc_data)
    if r.status_code != requests.codes.ok:
        return False

    # from rocketchat_API.rocketchat import RocketChat
    # chat_ip_port = "http://0.0.0.0:3000"
    # rocket = RocketChat('Admin', 'chat.service', server_url=chat_ip_port, proxies=None)
    # data = rocket.users_register(username+"@cit.com", username, password, username).json()
    # status = data['success']
    # print("user status ", status)
    return True


class UserManager:
    @staticmethod
    def update_user(username, updated_user):
        current = get_user(username)
        if current is None:
            # user does not exist
            return False
        current = current.to_dict()

        try:
            # check availability
            if username != updated_user.username:
                # username cannot be changed
                return False
        except AttributeError:
            # updated_user must have a username
            return False

        # check for connection fields
        current['username'] = updated_user.username
        try:
            if updated_user.password is not None:
                current['password'] = updated_user.password
        except AttributeError:
            # keep current value
            pass
        try:
            if updated_user.remote_ip is not None:
                current['remote_ip'] = updated_user.remote_ip
        except AttributeError:
            # keep current value
            pass

        # put data in the correct format
        conn_data = {
            'curr_username': username,
            'updated_username': current['username'],
            'new_password': current['password'],
            'new_ip': current['remote_ip']
        }
        # update connection info
        r = requests.put(connection_url, json=conn_data)
        if r.status_code != requests.codes.ok:
            return False

        updated_user = updated_user.to_dict()
        for k in updated_user:
            if updated_user[k] is not None:
                current[k] = updated_user[k]
        # put data in the correct format
        doc_data = {
            'collection_name': 'users',
            'document_id': username,
            'document': current
        }

        # store user in the database
        r = requests.put(database_url, json=doc_data)
        if r.status_code != requests.codes.ok:
            return False
        return True

    @staticmethod
    def delete_user(username):
        current = get_user(username)
        if current is None:
            # user does not exist
            return False

        # put data in the correct format
        data = {
            'list_of_users': [username]
        }
        # delete from connections, vpn will no longer be available
        r = requests.delete(connection_url, json=data)
        if r.status_code != requests.codes.ok:
            return False

        # put data in the correct format
        doc_data = {
            'collection_name': 'users',
            'document_id': username
        }
        # delete user from database
        r = requests.delete(database_url, json=doc_data)
        if r.status_code != requests.codes.ok:
            return False
        return True
