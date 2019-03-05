import sys, os, abc

from Platform import Platform

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class is a subclass of platform. This class will implement the tiddlywiki platform. 
    """

class TiddlyWiki(Platform):
    # fill the values here for your specific platform
    platform_name = "tiddly wiki"
    platform_start_command = "http-server /home/practicum/Documents/tiddlywikis/genericWiki/output"
    platform_end_command = "kill 1200"
    platform_version = "5.1.20-prerelease"
    platformInstallation = "/installation"
    port = "8085"
    ip = "0.0.0.0"
    link = "tiddly.com"
    # the fields below will be generated by Platform Manager
    processID = 0
    platform_id = "10"
    subplatforms = {"chat", "wiki"}

    #returns link to connect to website
    def getLink(self):
        return link 
    #returns ip and port to connect to website
    def getIpPort(self):
        return self.ip + ":" + self.port
    #returns platform name
    def getPlatformName(self):
        return self.getPlatformName
    
    #returns where the platforms installation path
    def getPlatformInstallation(self):
        return self.platformInstallation
    
    #return the version of the platform 
    def getPlatformVersion(self):
        return self.platform_version
    
    #return a platformID. You can pick a random value for this field.
    def getPlatformID(self):
        return self.platform_id
    # return command that starts platform
    def get_start_command(self):
        return self.platform_Start_Command + " -a " + ip + " -p " + port 

    #returns command to stop platform
    def get_stop_command(self):
        return self.platform_end_command + str(self.processID + 1)
    
    # returns list of subplatforms
    def get_sub_platforms(self):
        return self.subplatforms
    
    def handleRequest(self, jsonObject):
        pass
    
    
    #add more methods below if you need to do more tasks



