import sys, os, abc
from .Platform import Platform

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class RapidCyber(Platform):
    # fill the values here for your specific platform
    platform_name = "RapidCyber"
    platform_start_command = ""
    platform_end_command = ""
    platform_version = ""
    ip = ""
    port = ""
    link = ""
    # the fields below will be generated by Platform Manager
    platform_id = 0
    processID = 0
    subplatforms = {}

    staticPlatform = True
    #return process ID 
    def getProcessID(self):
        return self.processID

    #returns link to connect to website
    def getLink(self):
        return self.link 
    #returns ip and port to connect to website
    def getIpPort(self):
        return self.ip + ":" + self.port

    #returns platform name
    def getPlatformName(self):
        return self.platform_name
    
    #returns where the platforms installation path
    def getPlatformInstallation(self):
        return self.platform_id
    
    #return the version of the platform 
    def getPlatformVersion(self):
        return self.platform_version
    
    #return a platformID. You can pick a random value for this field.
    def getPlatformID(self):
        return self.platform_id
    # return command that starts platform
    def get_start_command(self):
        return self.platform_start_command

    #returns command to stop platform
    def get_stop_command(self):
        return self.platform_end_command
    
    # returns list of subplatforms
    def get_sub_platforms(self):
        return self.subplatforms
    
    #sets process ID 
    def setProcessID(self, processID):
        self.processID = processID

    #set link to connect to website
    def setLink(self, link):
        self.link = link
    
    #set ip and port to connect to website
    def setIpPort(self, ip, port):
        self.ip = ip 
        self.port = port 
    
    #set platform name
    def setPlatformName(self, platform_name):
        self.platform_name = platform_name 
    
    #set where the platforms installation path
    def setPlatformInstallation(self, platformInstallation):
        self.platformInstallation = platformInstallation 
    
    #set the version of the platform 
    def setPlatformVersion(self, platform_version):
        self.platform_version = platform_version
    
    #set a platformID. You can pick a random value for this field.
    def setPlatformID(self, PlatformID):
        self.platform_id = PlatformID
    
    # set command that starts platform
    def set_start_command(self, platform_start_command):
        self.platform_start_command = platform_start_command

    #set command to stop platform
    def set_stop_command(self, platform_end_command):
        self.platform_end_command = platform_end_command
    
    # set list of subplatforms
    def set_sub_platforms(self, subplatforms):
        self.subplatforms = subplatforms
    
    def requestHandler(self, jsonObject):
        pass
    
    
    #add more methods below if you need to do more tasks
