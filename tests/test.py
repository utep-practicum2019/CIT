import requests, json, unittest
import json as simplejson

#Test Accounts API

class test(unittest.TestCase):
    # def test_create_groups(self):
    #     print('Test create group | (POST) Input  <required fields>')
    #     data = {'group_count': 2,
    #             'users_per_group':5}
    #     local_url = "http://localhost:5000/api/v2/resources/group"
    #     r = requests.post(local_url, json=data)
    #     print(r.text)
    #     self.assertIn("true", r.text)
    #
    def test_update_group(self):
        print('Test group | (PUT) Input  <required fields>')
        data = {'group_id': 71,
                'updated_group': {
                    'group_id': 5
                }}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    # def test_add_users(self):
    #     print('Test add users | (POST) Input  <required fields>')
    #     data = {'users_per_group' : 3,
    #             'group_count' : 1}
    #     local_url = "http://localhost:5000/api/v2/resources/group"
    #     r = requests.post(local_url, json=data)
    #     print(r.text)
    #     self.assertIn("true", r.text)

    # def test_update_user_connection(self):
    #     print('Test update user connection| (PUT) Input  <required fields>')
    #     data = {"currUsername" : "user270",
    #             "newUsername" : "user500",
    #             "newPassword" : "password10",
    #             "newIP" : "192.168.1.1"}
    #     local_url = "http://localhost:5000/api/v2/resources/connection"
    #     r = requests.put(local_url, json=data)
    #     print(r.text)
    #     self.assertIn("true", r.text)

    # def test_update_user(self):
    #     print('Test user | (PUT) Input  <required fields>')
    #     data = {'username' : 'user364',
    #             'updated_user' : {
    #                 'username': 'root',
    #                 'group_id': 51
    #                 }
    #     }
    #     local_url = "http://localhost:5000/api/v2/resources/user"
    #     r = requests.put(local_url, json=data)
    #     print(r.text)
    #     self.assertIn("true", r.text)

if __name__ == '__main__':
    print ("TEST ")
    unittest.main()