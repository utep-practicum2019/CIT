import requests, json, unittest
import json as simplejson

#This class test vm config commands
class testVMs_Config(unittest.TestCase):

    def test0(self):
        print('Test no input')
        data = {}
        data_json = simplejson.dumps(data)
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        assert r.text.__contains__("No input data provided")

    #@unittest.skip("vmName gets set to none")
    def test1(self):
        print('Test 1 | vmName: no input')
        data = {"vmName": ""}
        data_json = simplejson.dumps(data)
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertNotIn("vmname  ", r.text)

    def test2(self):
        print('Test 2 | vmName: input')
        data = {"vmName": "hello"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("vmname hello", r.text)

    def test3(self):
        print('Test 3 | source ip: no input')
        data = {"src_ip": ""}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid IP address", r.text)

    def test4(self):
        print('Test 4 | source ip: wrong format 1')
        data = {"src_ip": "123"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid IP address", r.text)

    def test5(self):
        print('Test 5 | source ip: wrong format 2')
        data = {"src_ip": "1.23.6"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid IP address", r.text)

    def test6(self):
        print('Test 6 | source ip: letters')
        data = {"src_ip": "ipformat"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid IP address", r.text)

    def test7(self):
        print('Test 7 | source ip: correct format')
        data = {"src_ip": "192.168.0.1"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("src_ip 192.168.0.1", r.text)

    def test8(self):
        print('Test 8 | source port: no input')
        data = {"src_prt": ""}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid port", r.text)

    def test9(self):
        print('Test 9 | source port: letters')
        data = {"src_prt": "abc"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid port", r.text)

    def test10(self):
        print('Test 10 | source port: correct input')
        data = {"src_prt": "8080"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("src_prt8080", r.text)

    def test11(self):
        print('Test 11 | destination ip: no input')
        data = {"dst_ip": ""}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid IP address", r.text)

    def test12(self):
        print('Test 12 | destination ip: wrong format 1')
        data = {"dst_ip": "123"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid IP address", r.text)

    def test13(self):
        print('Test 13 | destination ip: wrong format 2')
        data = {"dst_ip": "1.23.6"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid IP address", r.text)

    def test14(self):
        print('Test 14 | destination ip: letters')
        data = {"dst_ip": "ipformat"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid IP address", r.text)

    def test15(self):
        print('Test 15 | destination ip: correct format')
        data = {"dst_ip": "192.168.0.1"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("dst_ip 192.168.0.1", r.text)


    def test16(self):
        print('Test 16 | destination port: no input')
        data = {"dst_prt": ""}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid port", r.text)

    def test17(self):
        print('Test 17 | destination port: letters')
        data = {"dst_prt": "abc"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid port", r.text)

    def test18(self):
        print('Test 18 | destination port: correct input')
        data = {"dst_prt": "8080"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("dst_prt 8080", r.text)

    def test19(self):
        print('Test 19 | adaptor number: no input')
        data = {"adpt_number": ""}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid input", r.text)

    def test20(self):
        print('Test 20 | adaptor number: letter input')
        data = {"adpt_number": "abc"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("Not a valid input", r.text)

    def test21(self):
        print('Test 21 | adaptor number: numerical input')
        data = {"adpt_number": "3"}
        local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
        r = requests.post(local_url, json=data)
        print(r.text)
        self.assertIn("adpt_number 3", r.text)


if __name__ == '__main__':
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    print ("TEST - VMs Config Command")
    unittest.main()
