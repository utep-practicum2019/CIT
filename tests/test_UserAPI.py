import requests, json
import json as simplejson

#Test User API

def test1():
    print ('Test 1 | (GET) No input')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text
    #print data

def test2():
    print ('Test 2 | (GET) Only username <required>')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = { 'username': 'user2'}
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text

def test3():
    print ('Test 3 | (GET) Only password <required>')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = { 'password': 'pass123'}
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text

def test4():
    print ('Test 4 | (GET) Username & password <required>')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = { 'username': 'user2',
             'password': 'password1',}
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text

def test5():
    print ('Test 5 | (GET) Required fields and some (ip & group id)')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = {'username': 'root',
            'password': 'toor',
            'group_id': 0,
            'internalIP': '192.168.0.1'}
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text

def test6():
    print ('Test 6| (GET) All fields')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = {'username': 'root',
            'password': 'toor',
            'group_id': 4,
            'internalIP': '192.168.0.1',
            'connectionType': 'vpn',
            'required': False }
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text

def test7():
    print ('Test 7 | (POST) No input')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test8():
    print ('Test 8 | (POST) Input  <only required fields>')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = {'username': 'root',
            'password': 'toor'}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test9():
    print ('Test 9 | (PUT) No input')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.put(local_url, json=data)
    print r.text

def test10():
    print ('Test 10 | (PUT) Input  <only required fields>')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = {'username': 'root',
            'password': 'toor'}
    data_json = simplejson.dumps(data)
    r = requests.put(local_url, json=data)
    print r.text

def test11():
    print ('Test 11 | (DELETE) No input')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.delete(local_url, json=data)
    print r.text

def test12():
    print ('Test 12 | (DELETE) Input <only required fields>')
    local_url = "http://localhost:5000/api/v2/resources/user"
    data = {'username': 'root',
            'password': 'toor'}
    data_json = simplejson.dumps(data)
    r = requests.delete(local_url, json=data)
    print r.text

if __name__ == '__main__':
    print ("TEST - User API")
    #GET
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    #POST
    test7()
    test8()
    #PUT
    test9()
    test10()
    #DELETE
    test11()
    test12()