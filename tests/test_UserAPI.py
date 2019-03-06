import requests, json, unittest
import json as simplejson

#Test User API

class test_UserAPI(unittest.TestCase):
    def test1(self):
        print('Test 1 | (GET) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test2(self):
        print('Test 2 | (GET) Only username <required>')
        data = {'username': 'user2'}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("connectionType", r.text)
        self.assertIn("remote_ip", r.text)

    def test3(self):
        print('Test 3 | (GET) Only password')
        data = {'password': 'pass123'}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field.", r.text)

    def test4(self):
        print('Test 4 | (GET) Username & password <required>')
        data = {'username': 'user2',
                'password': 'password1', }
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("connectionType", r.text)
        self.assertIn("remote_ip", r.text)

    def test5(self):
        print('Test 5 | (GET) Required fields and some (ip & group id)')
        data = {'username': 'root',
                'group_id': 0,
                'internalIP': '192.168.0.1'}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("connectionType", r.text)
        self.assertIn("remote_ip", r.text)

    def test6(self):
        print('Test 6| (GET) All fields')
        data = {'username': 'root',
                'password': 'toor',
                'group_id': 4,
                'internal_ip': '192.168.0.1',
                'remote_ip' : '192.168.0.2',
                'connectionType': 'vpn',
                'required': False}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("connectionType", r.text)
        self.assertIn("remote_ip", r.text)

    def test7(self):
        print('Test 7 | (POST) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test8(self):
        print('Test 8 | (POST) Input  <only required fields>')
        data = {'group_count': 8,
                'users_per_group': 5}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test9(self):
        print('Test 9 | (PUT) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test10(self):
        print('Test 10 | (PUT) Input  <only required fields>')
        data = {'username' : 'user1',
                'updated_user' : {
                    'username': 'root',
                    'password': 'toor',
                    'group_id': 4,
                    'internal_ip': '192.168.0.1',
                    'remote_ip' : '192.168.0.2',
                    'connectionType': 'vpn'},
        }
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertNotIn("Missing data for required field", r.text)


    def test11(self):
        print('Test 11 | (DELETE) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test12(self):
        print('Test 12 | (DELETE) Input <only required fields>')
        data = {'username': 'root'}
        local_url = "http://localhost:5000/api/v2/resources/user"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)


if __name__ == '__main__':
    local_url = "http://localhost:5000/api/v2/resources/user"
    print ("TEST - User API")
    unittest.main()

