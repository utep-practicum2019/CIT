import requests, json,unittest
import json as simplejson

#Test Login API
class test_LoginAPI(unittest.TestCase):

    def test1(local_url):
        print('Test 1 | (POST) No input, no credentials')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/login"
        r = requests.post(local_url, json=data)
        print(r.text)
        assert r.text.__contains__("Unauthorized access"), "missing credentials"
        # print data

    def test2(local_url):
        print('Test 2 | (POST) No input, credentials')
        data = {}
        local_url = "http://localhost:5000/api/v2/resources/login"
        r = requests.post(local_url, auth=('root', 'toor'), json=data)
        print(r.text)
        assert r.text.__contains__("No input data provided")

    def test3(local_url):
        print('Test 3 | (POST) Required input <wrong1>, credentials')
        data = {'ip': '192.16'}
        local_url = "http://localhost:5000/api/v2/resources/login"
        r = requests.post(local_url, auth=('root', 'toor'), json=data)
        print(r.text)
        assert r.text.__contains__("Not a valid IP address")

    def test4(local_url):
        print('Test 4 | (POST) Required input <wrong2>, credentials')
        data = {'ip': 'asdf'}
        local_url = "http://localhost:5000/api/v2/resources/login"
        r = requests.post(local_url, auth=('root', 'toor'), json=data)
        print(r.text)
        assert r.text.__contains__("Not a valid IP address")

    def test5(local_url):
        print('Test 5 | (POST) Required input <correct>, credentials')
        data = {'ip': '192.168.1.1'}
        local_url = "http://localhost:5000/api/v2/resources/login"
        r = requests.post(local_url, auth=('root', 'toor'), json=data)
        print(r.text)
        assert r.text.__contains__("Authenticated User")

if __name__ == '__main__':
    #local_url = "http://localhost:5000/api/v2/resources/login"
    print ("TEST - Login API")
    unittest.main()
