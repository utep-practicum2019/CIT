import sys
import os
import threading
import abc
import time
import subprocess

from .Platform import Platform

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to start, stop, and configure Chat platform.
    """


class RocketChat(Platform):
    # fill the values here for your specific platform
    platform_name = "Rocket.Chat"
    platform_start_command = "service snap.rocketchat-server.rocketchat-server start"
    platform_end_command = "service snap.rocketchat-server.rocketchat-server stop"
    platform_version = ""
    # the fields below will be generated by Platform Manager
    platform_id = ""
    subplatforms = {}
    port = ""
    ip = ""
    link = ""


    #returns link to connect to website
    def getLink(self):
        return link

    #returns ip and port to connect to website
    def getIpPort(self):
        return self.ip + ":" + self.port

    # returns platform name
    def getPlatformName(self):
        return self.getPlatformName

    # returns where the platforms installation path
    def getPlatformInstallation(self):
        return self.getPlatformInstallation

    # return the version of the platform
    def getPlatformVersion(self):
        return self.platform_version

    # return a platformID. You can pick a random value for this field.
    def getPlatformID(self):
        return self.platform_id

    # return command that starts platform
    def get_start_command(self):
        return self.platform_Start_Command

    # returns command to stop platform
    def get_stop_command(self):
        return self.platform_end_command

    # returns list of subplatforms
    def get_sub_platforms(self):
        return self.subplatforms

    def handleRequest(self, jsonObject):
        pass

    # add more methods below if you need to do more tasks

    hackathon_base_url = "http://localhost:3000"
    rcr_base_url = "http://localhost:3001"
    register = "/api/v1/users.register"
    login = "/api/v1/login"
    group = "/api/v1/groups.create"

    def POST(self, url, fields={}, headers=None):
        if not headers:
            headers = self.headers
        http = urllib3.PoolManager()
        r = http.request(
            "POST", url,
            body=json.dumps(fields),
            headers=headers)
        try:
            d = json.loads(r.data.decode('utf8'))
        except:
            print(r.data)
        return d

    def hackathon_register_user(self, hackathon_base_url, register, username, email, passw, name):
        url = hackathon_base_url + register
        data = {
            "username": username,
            "email": email,
            "pass": passw,
            "name": name
        }
        headers = {'Content-type': 'application/json'}
        d = self.POST(url, data, headers)
        print(d['_id'])

    def hackathon_login_user(self, hackathon_base_url, login, user, password):
        url = hackathon_base_url + login
        data = {"user": user,
                "password": password}

        headers = {'Content-Type': 'application/json'}
        d = self.POST(url, data, headers)
        userId = d['data']['userId']
        authToken = d['data']['authToken']
        headers = {
            "X-Auth-Token": authToken,
            "X-User-Id": userId
        }
        return headers

    # @staticmethod
    def hackathon_group_user(self, hackathon_base_url, group, name, members):
        url = hackathon_base_url + group
        data = {"name": name,
                "members": members}

        d = self.POST(url, fields=data)
        if d['success'] is True:
            print(d)
            raise ("Error Creating Channel")
        else:
            return True