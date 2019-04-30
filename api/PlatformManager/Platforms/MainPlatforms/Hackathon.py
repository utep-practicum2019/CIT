import sys, os, abc

from .Platform import Platform

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class is a subclass of platform. This class will implement the tiddlywiki platform. 
    """

class Hackathon(Platform):
    # fill the values here for your specific platform
    platform_name = "Hackathon"
    platform_alias = ""
    platform_note = ""
    platform_date_created = ""
    platform_start_command = " "
    platform_end_command = " "
    platform_version = " "
    platformInstallation = " "
    port = "7070"
    ip = "0.0.0.0"
    link = ""
    # the fields below will be generated by Platform Manager
    processID = 0
    platform_id = 0
    subplatforms = {" ", " "}

    staticPlatform = True

    #return process ID 
    def getProcessID(self):
        return self.processID

    #get link to connect to website
    def getLink(self):
        return self.link

    #get ip and port to connect to website
    def getIpPort(self):
        return self.ip + ":" + self.port

    #get platform name
    def getPlatformName(self):
        return self.platform_name
        
    #get platform alias
    def getPlatformAlias(self):
        return self.platform_alias

    #get platform note
    def getPlatformNote(self):
        return self.platform_note

    #get platform creation date
    def getPlatformDateCreated(self):
        return self.platform_date_created

    #get where the platforms installation path
    def getPlatformInstallation(self):
        return self.platformInstallation
    
    #get the version of the platform 
    def getPlatformVersion(self):
        return self.platform_version
    
    #get a platformID. You can pick a random value for this field.
    def getPlatformID(self):
        return int(self.platform_id)
    
    #gets command that starts platform
    def get_start_command(self):
        return self.platform_start_command 

    #get command to stop platform
    def get_stop_command(self):
        return self.platform_end_command + str(self.processID + 1)
    
    #get list of subplatforms
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

    #set platform alias
    def setPlatformAlias(self, alias):
        self.platform_alias = alias 

    #set platform note
    def setPlatformNote(self, note):
        self.platform_note = note

    #set platform creation date
    def setPlatformDateCreated(self, date):
        self.platform_date_created = date
    
    #set where the platforms installation path
    def setPlatformInstallation(self, platformInstallation):
        self.platformInstallation = platformInstallation 
    
    #return the version of the platform 
    def setPlatformVersion(self, platform_version):
        self.platform_version = platform_version
    
    #return a platformID. You can pick a random value for this field.
    def setPlatformID(self, PlatformID):
        self.platform_id = PlatformID
    
    # return command that starts platform
    def set_start_command(self, platform_start_command):
        self.platform_start_command = platform_start_command

    #set command to stop platform
    def set_stop_command(self, platform_end_command):
        self.platform_end_command = platform_end_command
    
    # set list of subplatforms
    def set_sub_platforms(self, subplatforms):
        self.subplatforms = subplatforms

    def requestHandler(self, jsonObject):
        print("Handling Request")
    
    
    #add more methods below if you need to do more tasks

