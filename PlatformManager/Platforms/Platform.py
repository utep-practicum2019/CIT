import sys
import os 
import abc

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes

        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class Platform(abc.ABC):
    
    platform_name = ""
    platform_start_command = ""
    platform_end_command = ""
    platform_version = ""
    port = ""
    ip = ""
    link = ""
    platform_id = ""
    processID = 0
    subplatforms = {}

    @abc.abstractmethod
    def getLink(self):
        pass
    @abc.abstractmethod
    def getIpPort(self):
        pass
    @abc.abstractmethod
    def getPlatformName(self):
        pass
    
    @abc.abstractmethod
    def getPlatformInstallation(self):
        pass
    
    @abc.abstractmethod
    def getPlatformVersion(self):
        pass
    
    @abc.abstractmethod
    def getPlatformID(self):
        pass
    @abc.abstractmethod
    def get_start_command(self):
        pass
    @abc.abstractmethod
    def get_stop_command(self):
        pass
    
    @abc.abstractmethod
    def get_sub_platforms(self):
        pass
    @abc.abstractmethod
    def requestHandler(self):
        pass




   
