import requests, json, unittest
import json as simplejson

#Test Platform API

class test_PlatformAPI(unittest.TestCase):
    def test0(self):
        print('Test 0 | (GET) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.get(local_url, json=data)
        print(r.text)
        self.assertIn("The method is not allowed for the requested URL", r.text)

    def test1(self):
        print('Test 1 | (POST) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test2(self):
        print('Test 2 | (POST) Blank fields')
        data = {'': ''}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test3(self):
        print('Test 3 | (POST) Input: Only one required field')
        data = {'platform_name': 'P1'}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test4(self):
        print('Test 4 | (POST) Input: All required fields')
        data = {'platform_name': 'P1',
                'file_path': 'file...',
                'ip_address': '192.168.0.1',
                'port': '5555'}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test5(self):
        print('Test 5 | (POST) Input: All fields')
        data = {'platform_name': 'P1',
                'file_path': 'file...',
                'ip_address': '192.168.0.1',
                'port': '5555',
                'command': 'command Name',
                'platform_id': 5}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test6(self):
        print('Test 6 | (PUT) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)


    def test7(self):
        print('Test 7 | (PUT) Blank fields')
        data = {'': ''}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test8(self):
        print('Test 8 | (PUT) Input: Only one required field')
        data = {'file_path': 'P8'}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test9(self):
        print('Test 9 | (PUT) Input: All required fields')
        data = {'platform_name': 'P1',
                'file_path': 'file...',
                'ip_address': '192.168.0.1',
                'port': '5555',
                'platform_id' : 3}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertNotIn("Missing data for required field", r.text)

    def test10(self):
        print('Test 10 | (PUT) Input: All fields')
        data = {'platform_name': 'P1',
                'file_path': 'file...',
                'ip_address': '192.168.0.1',
                'port': '5555',
                'command': 'command Name',
                'platform_id': 5}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.put(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test11(self):
        print('Test 11 | (DELETE) No input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test12(self):
        print('Test 12 | (DELETE) Blank fields')
        data = {'': ''}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test13(self):
        print('Test 13 | (DELETE) Input: Only one required field')
        data = {'file_path': 'P8'}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test14(self):
        print('Test 14 | (DELETE) Input: All required fields')
        data = {'platform_name': 'P1',
                'file_path': 'file...',
                'ip_address': '192.168.0.1',
                'port': '5555'}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test15(self):
        print('Test 15 | (DELETE) Input: All fields')
        data = {'platform_name': 'P1',
                'file_path': 'file...',
                'ip_address': '192.168.0.1',
                'port': '5555',
                'command': 'command Name',
                'platform_id': 5}
        local_url = "http://localhost:5000/api/v2/resources/platform"
        r = requests.delete(local_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

if __name__ == '__main__':
    local_url = "http://localhost:5000/api/v2/resources/platform"
    print ("TEST - Group API")
    unittest.main()
