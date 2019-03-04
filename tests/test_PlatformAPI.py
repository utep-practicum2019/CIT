import requests, json
import json as simplejson

#Test Platform API

def test0():
    print ('Test 0 | (GET) No input')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text

def test1():
    print ('Test 1 | (POST) No input')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text
    #print data

def test2():
    print ('Test 2 | (POST) Blank fields')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'' : ''}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test3():
    print ('Test 3 | (POST) Input: Only one required field')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'platform_name' : 'P1'}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test4():
    print ('Test 4 | (POST) Input: All required fields')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'platform_name' : 'P1',
            'file_path' : 'file...',
            'ip_address' : '192.168.0.1',
            'port': '5555'}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test5():
    print ('Test 5 | (POST) Input: All fields')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'platform_name' : 'P1',
            'file_path' : 'file...',
            'ip_address' : '192.168.0.1',
            'port': '5555',
            'command' : 'command Name',
            'platform_id' : 5}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test6():
    print ('Test 6 | (PUT) No input')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.put(local_url, json=data)
    print r.text

def test7():
    print ('Test 7 | (PUT) Blank fields')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'': ''}
    data_json = simplejson.dumps(data)
    r = requests.put(local_url, json=data)
    print r.text

def test8():
    print ('Test 8 | (PUT) Input: Only one required field')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'file_path': 'P8'}
    data_json = simplejson.dumps(data)
    r = requests.put(local_url, json=data)
    print r.text

def test9():
    print ('Test 9 | (PUT) Input: All required fields')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'platform_name': 'P1',
            'file_path': 'file...',
            'ip_address': '192.168.0.1',
            'port': '5555'}
    data_json = simplejson.dumps(data)
    r = requests.put(local_url, json=data)
    print r.text

def test10():
    print ('Test 10 | (PUT) Input: All fields')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'platform_name': 'P1',
            'file_path': 'file...',
            'ip_address': '192.168.0.1',
            'port': '5555',
            'command': 'command Name',
            'platform_id': 5}
    data_json = simplejson.dumps(data)
    r = requests.put(local_url, json=data)
    print r.text


def test11():
    print ('Test 11 | (DELETE) No input')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.delete(local_url, json=data)
    print r.text

def test12():
    print ('Test 12 | (DELETE) Blank fields')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'': ''}
    data_json = simplejson.dumps(data)
    r = requests.delete(local_url, json=data)
    print r.text

def test13():
    print ('Test 13 | (DELETE) Input: Only one required field')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'file_path': 'P8'}
    data_json = simplejson.dumps(data)
    r = requests.delete(local_url, json=data)
    print r.text

def test14():
    print ('Test 14 | (DELETE) Input: All required fields')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'platform_name': 'P1',
            'file_path': 'file...',
            'ip_address': '192.168.0.1',
            'port': '5555'}
    data_json = simplejson.dumps(data)
    r = requests.delete(local_url, json=data)
    print r.text

def test15():
    print ('Test 15 | (DELETE) Input: All fields')
    local_url = "http://localhost:5000/api/v2/resources/platform"
    data = {'platform_name': 'P1',
            'file_path': 'file...',
            'ip_address': '192.168.0.1',
            'port': '5555',
            'command': 'command Name',
            'platform_id': 5}
    data_json = simplejson.dumps(data)
    r = requests.delete(local_url, json=data)
    print r.text

if __name__ == '__main__':
    print ("TEST - Group API")
    #GET
    test0()
    #POST
    test1()
    test2()
    test3()
    test4()
    test5()
    #PUT
    test6()
    test7()
    test8()
    test9()
    test10()
    #DELETE
    test11()
    test12()
    test13()
    test14()
    test15()