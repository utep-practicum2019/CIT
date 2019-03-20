import requests, json, unittest
import json as simplejson

#Test Accounts API

class test_AccountsAPI(unittest.TestCase):

    # Test User API
    def test_getUser_no_input(self):
        print('Test user | (GET) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    # def test2(self):
    #     print('Test 2 | (GET) Only username <required>')
    #     data = {'username': 'user2'}
    #     local_url = "http://localhost:5000/api/v2/resources/user"
    #     r = requests.get(local_url, json=data)
    #     print(r.text)
    #     self.assertIn("connectionType", r.text)
    #     self.assertIn("remote_ip", r.text)

    # def test6(self):
    #     print('Test 6| (GET) All fields')
    #     data = {'username': 'root',
    #             'password': 'toor',
    #             'group_id': 4,
    #             'internal_ip': '192.168.0.1',
    #             'remote_ip' : '192.168.0.2',
    #             'connectionType': 'vpn',
    #             'required': False}
    #     local_url = "http://localhost:5000/api/v2/resources/user"
    #     r = requests.get(local_url, json=data)
    #     print(r.text)
    #     self.assertIn("connectionType", r.text)
    #     self.assertIn("remote_ip", r.text)

    def test_update_user_no_input(self):
        print('Test user | (PUT) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_user(self):
        print('Test user | (PUT) Input  <required fields>')
        data = {'username' : 'user1',
                'updated_user' : {
                    'username': 'root',
                    'password': 'toor',
                    'group_id': 4,
                    'internal_ip': '192.168.0.1',
                    'remote_ip' : '192.168.0.2',
                    'connectionType': 'vpn'}
        }
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_user_missing_fields(self):
        print('Test user | (PUT) Input  <missing required fields>')
        data = {'username' : 'user1'}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_user_delete_no_input(self):
        print('Test user | (DELETE) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_user_delete(self):
        print('Test user | (DELETE) Input <required fields>')
        data = {'username': 'root'}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)


        ##TEST GROUPS

    def test_get_group_no_input(self):
        print('Test group | (GET) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_create_group_no_input(self):
        print('Test create group | (POST) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_create_groups(self):
        print('Test create group | (POST) Input  <required fields>')
        data = {'group_count': 8,
                'users_per_group': 5,
                'file_path': 'test/path/'}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_create_groups_missing_fields(self):
        print('Test create group | (POST) Input  <missing required fields>')
        data = {'group_count': 8,
                'users_per_group': 5}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_update_gruop_no_input(self):
        print('Test group | (PUT) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_update_group(self):
        print('Test group | (PUT) Input  <required fields>')
        data = {'group_id': 10,
                'updated_group': {
                    'group_id': 5,
                    'min': 5,
                    'max': 8,
                    'platforms': ['P1', 'P2'],
                    'members': ['M1', 'M2'],
                    'chat_id': 0
                }}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_update_group_missing_fields(self):
        print('Test group | (PUT) Input  <missing required fields>')
        data = {'group_id': 10}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_group_delete_no_input(self):
        print('Test group | (DELETE) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_group_delete(self):
        print('Test group | (DELETE) Input <required fields>')
        data = {'group_id': 10}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

##TEST PLATFORM ATTACHMENT

    def test_attach_platform_no_input(self):
        print('Test attach platform | (POST) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_attach_platform(self):
        print('Test attach platform | (POST) Input  <required fields>')
        data = {'group_id': 8,
                'platform_name': "chat"}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_attach_platform_missing_fields(self):
        print('Test attach platform| (POST) Input  <missing required fields>')
        data = {'group_id': 8}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_detach_platform_no_input(self):
        print('Test detach platform | (DELETE) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_detach_platform(self):
        print('Test detach platform | (DELETE) Input <required fields>')
        data = data = {'platform_name': "chat"}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)


if __name__ == '__main__':
    print ("TEST - Accounts API")
    unittest.main()

