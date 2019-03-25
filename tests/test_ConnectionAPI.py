import requests, json, unittest

#test connection management interface

class test_ConnectionAPI(unittest.TestCase):
    def test_get_no_input(self):
        print('Test get | (GET) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_add_users_no_input(self):
        print('Test add users | (POST) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_add_users(self):
        print('Test add users | (POST) Input  <required fields>')
        data = {'users_per_group' : 3,
                'group_count' : 1}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_delete_users_no_input(self):
        print('Test delete users | (DELETE) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_delete_user(self):
        print('Test delete user | (DELETE) Input <required fields>')
        data = {'list_of_users': ["user267", "user268"]}
        local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_update_user__connection_no_input(self):
        print('Test user connection | (PUT) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_update_user_connection(self):
        print('Test update user connection| (PUT) Input  <required fields>')
        data = {'currUsername' : "user269",
                'newUsername' : "user500",
                'newPassword' : "password10",
                'newIP' : "192.168.1.1"}
        local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_update_user_missing_fields(self):
        print('Test update user | (PUT) Input  <missing required fields>')
        data = {'curr_username' : 'user1'}
        local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_file_add_users_no_input(self):
        print('Test file add users | (POST) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_file_add_users(self):
        print('Test file add users | (POST) Input  <required fields>')
        data = {'usernames': ["user1", "user2","user3"]}
        local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("user", r.text)
        self.assertIn("password", r.text)
        self.assertIn("pptpIP", r.text)


##api doc methods missing

    #
    # def test_create_platform_fwrule_no_input(self):
    #     print('Test create firewall rule | (POST) No input')
    #     data = {}
    #     local_url = "http://localhost:5000/api/v2/resources/connection"
    #     r = requests.post(local_url, json=data)
    #     print(r.text)
    #     self.assertIn("No input data provided", r.text)
    #
    # def test_create_platform_fwrule(self):
    #     print('Test create firewall rule  | (POST) Input  <required fields>')
    #     data = {'ip_address': '192.168.1.2',
    #             'port': "1234"}
    #     local_url = "http://localhost:5000/api/v2/resources/connection"
    #     r = requests.post(local_url, json=data)
    #     print(r.text)
    #     self.assertIn("true", r.text)
    #
    # def test_remove_platform_fwrule_no_input(self):
    #     print('Test remove firewall rule| (DELETE) No input')
    #     data = {}
    #     local_url = "http://localhost:5000/api/v2/resources/connection"
    #     r = requests.delete(local_url, json=data)
    #     print(r.text)
    #     self.assertIn("false", r.text)
    #
    # def test_remove_platform_fw_rule(self):
    #     print('Test remove firewall rule | (DELETE) Input <required fields>')
    #     data = {'ip_address': '192.168.1.2',
    #             'port': "1234"}
    #     local_url = "http://localhost:5000/api/v2/resources/connection"
    #     r = requests.delete(local_url, json=data)
    #     print(r.text)
    #     self.assertIn("true", r.text)



if __name__ == '__main__':
    print ("TEST - Connections API")
    unittest.main()
