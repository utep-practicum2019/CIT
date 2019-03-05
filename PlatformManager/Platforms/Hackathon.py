import sys
import os
import abc
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

class Hackathon(Platform):

    # fill the values here for your specific platform
    platform_name = ""
    platform_start_command = ""
    platform_end_command = ""
    platform_version = ""
    # the fields below will be generated by Platform Manager
    platform_id = ""
    subplatforms = {}

    #returns platform name
    def getPlatformName(self):
        return self.getPlatformName
    
    #returns where the platforms installation path
    def getPlatformInstallation(self):
        return self.getPlatformInstallation
    
    #return the version of the platform 
    def getPlatformVersion(self):
        return self.platform_version
    
    #return a platformID. You can pick a random value for this field.
    def getPlatformID(self):
        return self.platform_id
    # return command that starts platform
    def get_start_command(self):
        return self.platform_Start_Command

    #returns command to stop platform
    def get_stop_command(self):
        return self.platform_end_command
    
    # returns list of subplatforms
    def get_sub_platforms(self):
        return self.subplatforms
    
    def requestHandler(self, jsonObject):
        pass
    
    
    #add more methods below if you need to do more tasks


