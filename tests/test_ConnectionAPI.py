import requests, json, unittest

#test connection management interface

connection_url = "http://citsystem.com/api/v2/resources/connection"

class test_ConnectionAPI(unittest.TestCase):
    def test_get_no_input(self):
        print('Test get | (GET) No input')
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.get(connection_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def update_session_list_true(self):
        print('Test update session list  | (GET) True')
        data = {"session_list" : 'True'}
        local_url = "http://localhost:5000/api/v2/resources/connection?session_list=True"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("usersDictionary", r.text)

    def update_session_list_true(self):
        print('Test update session list  | (GET) False')
        data = {"session_list" : 'True'}
        local_url = "http://localhost:5000/api/v2/resources/connection?session_list=False"
        r = requests.get(connection_url, json=data)
        print(r.text)
        self.assertIn("", r.text)

    def test_add_users_no_input(self):
        print('Test add users | (POST) No input')
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.post(connection_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_add_users(self):
        print('Test add users | (POST) Input  <required fields>')
        data = {'num_users' : 3}
        #local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(connection_url, json=data)
        print(r.text)
        self.assertIn("usersDictionary", r.text)

    def test_file_add_users_no_input(self):
        print('Test file add users | (POST) No input')
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.post(connection_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_file_add_users(self):
        print('Test file add users | (POST) Input  <required fields>')
        data = {'usernames': ["p1", "p2","p3"]}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.post(connection_url, json=data)
        print(r.text)
        self.assertIn("username", r.text)
        self.assertIn("password", r.text)
        self.assertIn("pptpIP", r.text)

    def test_delete_users_no_input(self):
        print('Test delete users | (DELETE) No input')
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.delete(connection_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_delete_user(self):
        print('Test delete user | (DELETE) Input <required fields>')
        data = {'list_of_users': ["user3_", "user4_"]}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.delete(connection_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_update_user_connection_no_input(self):
        print('Test user connection | (PUT) No input')
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(connection_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_update_user_connection(self):
        print('Test update user connection| (PUT) Input  <required fields>')
        data = {'curr_username' : "user6_",
                'new_username' : "user500",
                'new_password' : "password10",
                'new_ip' : "192.168.1.1"}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(connection_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_update_user_missing_fields(self):
        print('Test update user | (PUT) Input  <missing required fields>')
        data = {'curr_username' : 'user1'}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(connection_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_pptp_poll_conection_no_input(self):
        print('Test pptp poll connection | (PUT) No Input')
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(connection_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_pptp_poll_conection(self):
        print('Test pptp poll connection | (PUT) No Input')
        data = {"command": "start"}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(connection_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_stop_no_input(self):
        print('Test pptp poll connection | (PUT) No Input')
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(connection_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_stop(self):
        print('Test pptp poll connection | (PUT) No Input')
        data = {"command": "stop"}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(connection_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_inexistent_command(self):
        print('Test pptp poll connection | (PUT) No Input')
        data = {"command": "blah"}
        #local_url = "http://localhost:5000/api/v2/resources/connection"
        r = requests.put(connection_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)



if __name__ == '__main__':
    print ("TEST - Connections API")
    unittest.main()
