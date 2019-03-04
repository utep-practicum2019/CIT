import requests, json
import json as simplejson

#Test GROUP API

def test1():
    print ('Test 1 | (GET) No input')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text
    #print data

def test2():
    print ('Test 2 | (GET) Input: All fields <except required> ')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {'min': 0,
            'max': 0,
            'platforms': ['P1', 'P2'],
            'members': ['M1', 'M2'],
            'chat_id': 0,
            'success': True }
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text

def test3():
    print ('Test 3 | (GET) Input: Only group id <required field> ')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {'group_id': 2 }
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text

def test4():
    print ('Test 4 | (GET) Input: No fields ')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {'': ''}
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text

def test5():
    print ('Test 5 | (GET) Input: All fields ')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {'group_id': 5,
            'min': 5,
            'max': 8,
            'platforms': ['P1', 'P2'],
            'members': ['M1', 'M2'],
            'chat_id': 0,
            'success': True}
    data_json = simplejson.dumps(data)
    r = requests.get(local_url, json=data)
    print r.text

def test6():
    print ('Test 6 | (POST) No input')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test7():
    print ('Test 7 | (POST) Blank fields')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {"" : ""}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test8():
    print ('Test 8 | (POST) Input  <only required fields>')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {'group_id': 8}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test9():
    print ('Test 9 | (PUT) No input')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.put(local_url, json=data)
    print r.text

def test10():
    print ('Test 10 | (PUT) Input  <only required fields>')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {'group_id': 10}
    data_json = simplejson.dumps(data)
    r = requests.put(local_url, json=data)
    print r.text

def test11():
    print ('Test 11 | (DELETE) No input')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.delete(local_url, json=data)
    print r.text

def test12():
    print ('Test 12 | (DELETE) Input <only required fields>')
    local_url = "http://localhost:5000/api/v2/resources/group"
    data = {'group_id': 10}
    data_json = simplejson.dumps(data)
    r = requests.delete(local_url, json=data)
    print r.text



if __name__ == '__main__':
    print ("TEST - Group API")
    #GET
    test1()
    test2()
    test3()
    test4()
    test5()
    #POST
    test6()
    test7()
    test8()
    #PUT
    test9()
    test10()
    #DELETE
    test11()
    test12()
