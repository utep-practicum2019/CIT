import requests, json, unittest
import json as simplejson

#Test GROUP API

class test_GroupAPI(unittest.TestCase):
    def test1(self):
        print('Test 1 | (GET) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test2(self):
        print('Test 2 | (GET) Input: All fields <except required> ')
        data = {'min': 0,
                'max': 0,
                'platforms': ['P1', 'P2'],
                'members': ['M1', 'M2'],
                'chat_id': 0,
                'success': True}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test3(self):
        print('Test 3 | (GET) Input: Only group id <required field> ')
        data = {'group_id': 2}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("members", r.text)
        self.assertIn("platforms", r.text)

    def test4(self):
        print('Test 4 | (GET) Input: No fields ')
        data = {'': ''}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test5(self):
        print('Test 5 | (GET) Input: All fields ')
        data = {'group_id': 5,
                'min': 5,
                'max': 8,
                'platforms': ['P1', 'P2'],
                'members': ['M1', 'M2'],
                'chat_id': 0,
                'success': True}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("members", r.text)
        self.assertIn("platforms", r.text)
        self.assertIn("group_id", r.text)

    def test6(self):
        print('Test 6 | (POST) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test7(self):
        print('Test 7 | (POST) Blank fields')
        data = {"": ""}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test8(self):
        print('Test 8 | (POST) Input  <only required fields>')
        data = {'group_id': 8}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test9(self):
        print('Test 9 | (PUT) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test10(self):
        print('Test 10 | (PUT) Input  <only required fields>')
        data = {'group_id': 10,
                'updated_group': {
                    'group_id': 5,
                    'min': 5,
                    'max': 8,
                    'platforms': ['P1', 'P2'],
                    'members': ['M1', 'M2'],
                    'chat_id': 0,
                    'success': True
                }}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertNotIn("Invalid input type", r.text)

    def test11(self):
        print('Test 11 | (DELETE) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test12(self):
        print('Test 12 | (DELETE) Input <only required fields>')
        data = {'group_id': 10}
        local_url = "http://localhost:5000/api/v2/resources/group"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)


if __name__ == '__main__':
    local_url = "http://localhost:5000/api/v2/resources/group"
    print ("TEST - Group API")
    unittest.main()
