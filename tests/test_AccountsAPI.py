import requests, json, unittest
import json as simplejson

#Test Accounts API

users_url = "http://citsystem.com/api/v2/resources/user"
group_url = "http://citsystem.com/api/v2/resources/group"



class test_AccountsAPI(unittest.TestCase):
    # # Test User API
    def test_getUser_no_input(self):
        print('Test user | (GET) No input')
        data = {}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/user"
        r = requests.get(users_url, json=data)
        print(r.text)
        self.assertIn("username", r.text)

    def test_getUser(self):
        print('Test user | (GET) ')
        data = {"username" : "user1_"}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/user"
        r = requests.get(users_url, json=data)
        print(r.text)
        self.assertIn("group_id", r.text)
        self.assertIn("username", r.text)
        self.assertIn("password", r.text)


    def test_update_user_no_input(self):
        print('Test user | (PUT) No input')
        data = {}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/user"
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_update_user(self):
        print('Test user | (PUT) Input  <required fields>')
        data = {'username' : 'user135',
                'updated_user' : {
                    'username': 'root',
                    'password': 'toor',
                    'group_id': 5,
                    'internal_ip': '192.168.0.1',
                    'remote_ip' : '192.168.0.2',
		    'alias': 'heyboy',
		    'note': 'user updated'
                }
        }
        #local_url = "http://0.0.0.0:5001/api/v2/resources/user"
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_user_missing_fields(self):
        print('Test user | (PUT) Input  <missing required fields>')
        data = {'username' : 'user136',
                'updated_user': {
                    'password': 'toor',
                    'group_id': 5,
                    'internal_ip': '192.168.0.1'
                }
        }
        #local_url = "http://0.0.0.0:5001/api/v2/resources/user"
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test_user_delete_no_input(self):
        print('Test user | (DELETE) No input')
        data = {}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/user"
        r = requests.delete(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_user_delete(self):
        print('Test user | (DELETE) Input <required fields>')
        data = {'list_of_users': ['user1_', 'user2_']}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/user"
        r = requests.delete(users_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)


        ##TEST GROUPS

    def test_get_group_no_input(self):
        print('Test group | (GET) No input')
        data = {}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/group"
        r = requests.get(group_url, json=data)
        print(r.text)
        self.assertIn("members", r.text)

    def test_get_group(self):
        print('Test group | (GET)')
        data = {"group_id" : 1}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/group"
        r = requests.get(group_url, json=data)
        print(r.text)
        self.assertIn("group_id", r.text)
        self.assertIn("max", r.text)
        self.assertIn("min", r.text)

    def test_create_group_no_input(self):
        print('Test create group | (POST) No input')
        data = {}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/group"
        r = requests.post(group_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_create_groups(self):
        print('Test create group | (POST) Input  <required fields>')
        data = {'group_count': 2,
                'users_per_group': 3}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/group"
        r = requests.post(group_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_create_groups_missing_fields(self):
        print('Test create group | (POST) Input  <missing required fields>')
        data = {'users_per_group': 5}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/group"
        r = requests.post(group_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)


    def test_update_group_no_input(self):
        print('Test group | (PUT) No input')
        data = {}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/group"
        r = requests.put(group_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_update_group(self):
        print('Test group | (PUT) Input  <required fields>')
        data = {
            "group_id" : 3,
            "updated_group" :
                {
                    "group_id": 3,
                    "min": 5,
                    "max": 8,
                    "platforms": ["TiddlyWiki"],
                    "members": [
                        "Pedro"
                    ],
                    "alias": "test",
                    "note": "test",
                }
        }
        #local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(group_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_update_group_missing_fields(self):
        print('Test group | (PUT) Input  <missing required fields>')
        data =  {
            "group_id" : 7,
            "updated_group" :
                {
                    "group_id": 7,
                    "min": 4,
                    "max": 7
                }
        }
        #local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(group_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_group_delete_no_input(self):
        print('Test group | (DELETE) No input')
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.delete(group_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_group_delete(self):
        print('Test group | (DELETE) Input <required fields>')
        data = {'list_of_groups': [2]}
        #local_url = "http://0.0.0.0:5001/api/v2/resources/group"
        r = requests.delete(group_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

##TEST PLATFORM ATTACHMENT

    def test_attach_platform_no_input(self):
        print('Test attach platform | (PUT) No input')
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(group_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_attach_platform(self):
        print('Test attach platform | (PUT) Input  <required fields>')
        data = {'group_id': 6,
                        'updated_group': {
                "command" : "attach",
                  "platform_ids": 61467}
                }
        #local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(group_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_attach_platform_missing_fields(self):
        print('Test attach platform| (PUT) Input  <missing required fields>')
        data = {'command': 'attach'}
        #local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(group_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test_detach_platform_no_input(self):
        print('Test detach platform |  No input')
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(group_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_detach_platform(self):
        print('Test detach platform | Input <required fields>')
        data = {'group_id': 6,
                        'updated_group': {
                             "group_id": 6,
                             "command" : "detach",
                             "platform_ids": 744}
                }
        #local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(group_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_detach_platform_missing_fields(self):
        print('Test detach platform | (DELETE) Input <required fields>')
        data = {'group_id': 6 }
        #local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(group_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

if __name__ == '__main__':
    print ("TEST - Accounts API")
    unittest.main()

