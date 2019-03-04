import requests, json
import json as simplejson

#This class test vm config commands

def test0():
    print ('Test no input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text
    #print data

def test1():
    print ('Test 1 | vmName: no input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"vmName": ""}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test2():
    print ('Test 2 | vmName: input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"vmName": "hello"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test3():
    print ('Test 3 | source ip: no input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"src_ip" : ""}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test4():
    print ('Test 4 | source ip: wrong format 1')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"src_ip" : "123"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test5():
    print ('Test 5 | source ip: wrong format 2')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"src_ip" : "1.23.6"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test6():
    print ('Test 6 | source ip: letters')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"src_ip" : "ipformat"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test7():
    print ('Test 7 | source ip: correct format')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"src_ip" : "192.168.0.1"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test8():
    print ('Test 8 | source port: no input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"src_prt" : ""}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test9():
    print ('Test 9 | source port: letters')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"src_prt" : "abc"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test10():
    print ('Test 10 | source port: correct input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"src_prt" : "8080"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test11():
    print ('Test 11 | destination ip: no input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"dst_ip": ""}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test12():
    print ('Test 12 | destination ip: wrong format 1')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"dst_ip": "123"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test13():
    print ('Test 13 | destination ip: wrong format 2')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"dst_ip": "1.23.6"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test14():
    print ('Test 14 | destination ip: letters')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"dst_ip": "ipformat"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test15():
    print ('Test 15 | destination ip: correct format')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"dst_ip": "192.168.0.1"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test16():
    print ('Test 16 | destination port: no input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"dst_prt": ""}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test17():
    print ('Test 17 | destination port: letters')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"dst_prt": "abc"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text


def test18():
    print ('Test 18 | destination port: correct input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"dst_prt": "8080"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test19():
    print ('Test 19 | adaptor number: no input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"adpt_number": ""}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test20():
    print ('Test 20 | adaptor number: letter input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"adpt_number": "abc"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

def test21():
    print ('Test 21 | adaptor number: numerical input')
    local_url = "http://localhost:5000/api/v2/resources/vm/manage/config"
    data = {"adpt_number": "3"}
    data_json = simplejson.dumps(data)
    r = requests.post(local_url, json=data)
    print r.text

if __name__ == '__main__':
    print ("TEST - VMs Config Command")
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
    test12()
    test13()
    test14()
    test15()
    test16()
    test17()
    test18()
    test19()
    test20()
    test21()
