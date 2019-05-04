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
    platform_alias = ""
    platform_note = ""
    platform_date_created = ""
    platform_start_command = ""
    platform_end_command = ""
    platform_version = ""
    port = ""
    ip = ""
    link = ""
    platform_id = 0
    processID = 0
    subplatforms = {}
    staticPlatform = True
    
    @abc.abstractmethod
    def getProcessID(self):
        pass

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
    def getPlatformAlias(self):
        pass

    @abc.abstractmethod
    def getPlatformNote(self):
        pass

    @abc.abstractmethod
    def getPlatformDateCreated(self):
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
    def setProcessID(self, processID):
        pass

    @abc.abstractmethod
    def setLink(self, link):
        pass
    
    @abc.abstractmethod
    def setIpPort(self, ip, port):
        pass
    
    @abc.abstractmethod
    def setPlatformName(self, platform_name):
        pass

    @abc.abstractmethod
    def setPlatformAlias(self, alias):
        pass

    @abc.abstractmethod
    def setPlatformNote(self, note):
        pass

    @abc.abstractmethod
    def setPlatformDateCreated(self, note):
        pass
    
    @abc.abstractmethod
    def setPlatformInstallation(self, platformInstallation):
        pass
    
    @abc.abstractmethod
    def setPlatformVersion(self, platform_version):
        pass
    
    @abc.abstractmethod
    def setPlatformID(self, PlatformID):
        pass
    
    @abc.abstractmethod
    def set_start_command(self, platform_start_command):
        pass

    @abc.abstractmethod
    def set_stop_command(self, platform_end_command):
        pass
    
    @abc.abstractmethod
    def set_sub_platforms(self, subplatforms):
        pass

    @abc.abstractmethod
    def requestHandler(self):
        pass
   
