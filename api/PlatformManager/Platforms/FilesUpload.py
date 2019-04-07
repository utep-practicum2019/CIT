import sys, os, abc
from shutil import *
from .Platform import Platform

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class is a subclass of platform. This class will implement the tiddlywiki platform. 
    """

class FilesUpload(Platform):
    # fill the values here for your specific platform
    platform_name = "FilesUpload"
    platform_start_command = " "
    platform_end_command = " "
    platform_version = " "
    platformInstallation = "../CIT/api/static/download_files"
    port = " "
    ip = " "
    link = ""
    # the fields below will be generated by Platform Manager
    processID = 0
    platform_id = 0
    subplatforms = { }

    uploads_path = '/home/practicum/Desktop'


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
        return self.platformInstallation
    
    #return the version of the platform 
    def getPlatformVersion(self):
        return self.platform_version
    
    #return a platformID. You can pick a random value for this field.
    def getPlatformID(self):
        return int(self.platform_id)
    # return command that starts platform
    def get_start_command(self):
       return  ""

    #returns command to stop platform
    def get_stop_command(self):
        return "" 
    
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
    
    #sets the version of the platform 
    def setPlatformVersion(self, platform_version):
        self.platform_version = platform_version
    
    # sets a platformID. You can pick a random value for this field.
    def setPlatformID(self, PlatformID):
        self.platform_id = PlatformID
    
    # sets command that starts platform
    def set_start_command(self, platform_start_command):
        self.platform_start_command = platform_start_command

    #set command to stop platform
    def set_stop_command(self, platform_end_command):
        self.platform_end_command = platform_end_command
    
    # set list of subplatforms
    def set_sub_platforms(self, subplatforms):
        self.subplatforms = subplatforms
        
    
    def requestHandler(self, jsonObject):
        fileMethods = {
        "addFile": self.addFile,
        "delFile" : self.delFile
        }
        return fileMethods[jsonObject["command"]](jsonObject["parameters"])
    
    def addFile(self, parameters):
        print("addFiles" + str(parameters))
        copy(parameters["filePath"], self.uploads_path)
        return "Success"

    def delFile(self, parameters):
        print("deleteFiles" + str(parameters))
        os.remove(self.uploads_path + "/" + parameters["file"])
        return "Success"
    
    def getFiles(self):
        print(os.path.dirname(os.path.abspath(__file__)))
