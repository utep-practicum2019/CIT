
import json
import requests
from pprint import pprint
from .Platform import Platform

from rocketchat_API.rocketchat import RocketChat

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to start, stop, and configure Chat platform.
    """


class Rocketchat(Platform):
    # fill the values here for your specific platform
    platform_name = "Rocketchat"
    platform_start_command = "echo 'toor' | sudo -S service snap.rocketchat-server.rocketchat-server start"
    platform_end_command = "echo 'toor' | sudo -S service snap.rocketchat-server.rocketchat-server stop"
    platform_version = ""
    # the fields below will be generated by Platform Manager
    platform_install = ""
    platform_id = 0
    processID = 0
    subplatforms = {}
    port = "3000"
    ip = "0.0.0.0"
    link = "http://www.chat.service"

    def __init__(self):
        
        self.proxy_dict = {
            "http": "http://localhost:3000",
            "https": "https://localhost:3001",
        }



        
    # return process ID
    def getProcessID(self):
        return self.processID

    # returns link to connect to website
    def getLink(self):
        return self.link

    # returns ip and port to connect to website
    def getIpPort(self):
        return self.ip + ":" + self.port

    # returns platform name
    def getPlatformName(self):
        return self.platform_name

    # returns where the platforms installation path
    def getPlatformInstallation(self):
        return self.platform_install

    # return the version of the platform
    def getPlatformVersion(self):
        return self.platform_version

    # return a platformID. You can pick a random value for this field.
    def getPlatformID(self):
        return self.platform_id

    # return command that starts platform
    def get_start_command(self):
        return self.platform_start_command

    # returns command to stop platform
    def get_stop_command(self):
        return self.platform_end_command

    # returns list of subplatforms
    def get_sub_platforms(self):
        return self.subplatforms

    def requestHandler(self, jsonObject):
        if jsonObject['command'] == 'chat_command':
            print("Success")
            return True

    # sets process ID
    def setProcessID(self, processID):
        self.processID = processID

    # set link to connect to website
    def setLink(self, link):
        self.link = link

    # set ip and port to connect to website
    def setIpPort(self, ip, port):
        self.ip = ip
        self.port = port

        # set platform name

    def setPlatformName(self, platform_name):
        self.platform_name = platform_name

        # set where the platforms installation path

    def setPlatformInstallation(self, platformInstallation):
        self.platformInstallation = platformInstallation

        # sets the version of the platform

    def setPlatformVersion(self, platform_version):
        self.platform_version = platform_version

    # sets a platformID. You can pick a random value for this field.
    def setPlatformID(self, PlatformID):
        self.platform_id = PlatformID

    # sets command that starts platform
    def set_start_command(self, platform_start_command):
        self.platform_start_command = platform_start_command

    # set command to stop platform
    def set_stop_command(self, platform_end_command):
        self.platform_end_command = platform_end_command

    # set list of subplatforms
    def set_sub_platforms(self, subplatforms):
        self.subplatforms = subplatforms

    # add more methods below if you need to do more tasks
    
    
    #Create a RocketChat object and login on the specified server:
    #rocket = RocketChat(user, passw , server_url='http://www.chat.service', proxies=None)


    #users = {useremail1: (userpass, usernick, ), useremail2}
    
    def registerUser(self, user_email, user_name, user_pass):
        rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
        data = rocket.users_register(user_email, user_name, user_pass, user_name).json()
        status = data['success']
        uId = data['user']['_id']
        return (status, uId)


    # Login a user: 
    def loginUser(self, user_name, user_pass):
        rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
        print(user_name + " " + user_pass)
        data = rocket.login(user_name, user_pass).json()
        status = data["status"]
        authToken = data["data"]["authToken"]
        print(status + " " + authToken)
        return (status, authToken)


    # Get User info:
    def getUserInfo(self, userID, user_name):
        rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
        data = rocket.users_info(userID, user_name).json()
        status = data["success"]
        uId = data['user']['_id']
        email = data['user']['emails'][0]['address']
        userName = data['user']['name']
        userNick = data['user']['username']
        return (status, uId, email, userName, userNick)


    # Delete a user:
    def deleteUser(self, userID):
        rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
        data = rocket.users_delete(userID).json()
        status = data["success"]
        return status


    # Create a new public channel optionally adding users:
    def createChannel(self, channelName):
        rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
        data = rocket.channels_create(channelName).json()
        status = data["success"]
        roomId = data["channel"]['_id']
        return (status, roomId)


    # Delete a public channel:
    def deleteChannel(self, roomId):
        rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
        data =  rocket.channels_delete(roomId).json()
        status = data["success"]
        return status


    # Create a new private group, optionally including users
    def createPrivateGroup(self, groupName):
        rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
        data = rocket.groups_create(groupName).json()
        status = data["success"]
        roomId = data["group"]['_id']
        return (status, roomId)


    # Delete a private group:
    def deletePrivateGroup(self, roomId):
        rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
        data = rocket.groups_delete(roomId).json()
        status = data["success"]
        return status


    # Set announcement for channel:
    def postNewMessage(self, roomID, announce):
        rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
        data = rocket.channels_set_announcement(roomID, announce).json()
        status = data["success"]
        msg = data["announcement"]
        return (status, msg)


    # Create User Token:
    def userToken(self, userID, user_name):
        rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
        data = rocket.users_create_token(userID, user_name).json()
        status = data["success"]
        token = data["data"]["authToken"]
        return (status, token)
'''
rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)
pprint(rocket.users_delete('h2uXXKrS4jnpkqa29').json())
'''
################################# TO DO IF NEEDED #############################################

# List all public channels:
# pprint(rocket.channels_list().json())

# List a public channel's memebers:
# pprint(rocket.channels_members(roomID).json())

# Get a public channel information:
# pprint(rocket.channels_info(roomID).json())

# Get public channel history:
# pprint(rocket.channels_history(roomID, count=5).json())

# List all users and related info:
# pprint(rocket.users_list().json())

# List all private groups with related information:
# pprint(rocket.groups_list_all().json())

# Get private group history:
# pprint(rocket.groups_history(roomID, count=5).json())

# Add user to a private group:
# pprint(rocket.groups_invite(roomID, userID).json())

# Remove user from a private group:
# pprint(rocket.groups_kick(roomID, userID).json())

# Get a private group information:
# pprint(rocket.groups_info(roomID).json())

# List of memebers of a private group:
# pprint(rocket.groups_memebers(roomID).json())

# Display Information about the Rocket.Chat server:
# pprint(rocket.info().json())

# Post a new Chat message:
# pprint(rocket.chat_post_message('good news everyone!', channel='GENERAL', alias='Farnsworth').json())

    