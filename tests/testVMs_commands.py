import requests, json
import json as simplejson

#Test vm status, suspend, and start commands

def test1():
    print ('Test 1 | Status: no input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/status"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text
    #print data

def test2():
    print ('Test 2 | Status: input name (blank)')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/status"
    data = {"vmName" : "vm1"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test3():
    print ('Test 3 | Status: input name')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/status"
    data = {"vmName" : "vm1"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test4():
    print ('Test 4 | Status: input name and mgrStatus')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/status"
    data = {"vmName" : "vm2",
            "mgrStatus" : "running"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test5():
    print ('Test 5 | Start: no input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/start"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test6():
    print ('Test 6 | Start: name input (blank)')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/start"
    data = {"vmName" : ""}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test7():
    print ('Test 7 | Start: name input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/start"
    data = {"vmName" : "vm1"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test8():
    print ('Test 8 | Suspend: no input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/suspend"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test9():
    print ('Test 9 | Suspend: vmname (blank)')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/suspend"
    data = {"vmName" : ""}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test10():
    print ('Test 10 | Suspend: vmname')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/suspend"
    data = {"vmName" : "vm10"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


if __name__ == '__main__':
    print ("TEST - VM Status Command")
    test1()
    test2()
    test3()
    test4()

    print ("TEST - VM Start Command")
    test5()
    test6()
    test7()

    print ("TEST - VM Suspend Command")
    test8()
    test9()
    test10()

