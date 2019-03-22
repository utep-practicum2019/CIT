import requests, json, unittest
import json as simplejson

#Test vm status, suspend, and start commands
class testVMs_commands(unittest.TestCase):
    def test1(self):
        print('Test 1 | Status: no input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/status"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test2(self):
        print('Test 2 | Status: input name (blank)')
        data = {"vmName": ""}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/status"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertNotIn("vmname  ", r.text)

    def test3(self):
        print('Test 3 | Status: input name')
        data = {"vmName": "vm1"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/status"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("vmname vm1", r.text)


    def test4(self):
        print('Test 4 | Status: input name and mgrStatus')
        data = {"vmName": "vm2",
                "mgrStatus": "running"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/status"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("vmname vm2 mgrstatus running", r.text)

    def test5(self):
        print('Test 5 | Start: no input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/start"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test6(self):
        print('Test 6 | Start: name input (blank)')
        data = {"vmName": ""}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/start"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertNotIn("vmname ", r.text)

    def test7(self):
        print('Test 7 | Start: name input')
        data = {"vmName": "vm1"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/start"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("vmname vm1", r.text)

    def test8(self):
        print('Test 8 | Suspend: no input')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/suspend"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test9(self):
        print('Test 9 | Suspend: vmname (blank)')
        data = {"vmName": ""}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/suspend"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertNotIn("vmname ", r.text)

    def test10(self):
        print('Test 10 | Suspend: vmname')
        data = {"vmName": "vm10"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/suspend"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("vmname vm10", r.text)


if __name__ == '__main__':
    print ("TEST - VM Status Command")
    unittest.main()


