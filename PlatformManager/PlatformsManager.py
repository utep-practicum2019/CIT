import sys
import os 
from yapsy.PluginManager import PluginManager
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

class PlatformManager(abc.ABC):
    pluginManager = PluginManager()
    
    @abc.abstractmethod
    def addPlatform(self):
        pass
    
    @abc.abstractmethod
    def removePlatform(self):
        pass
    
    @abc.abstractmethod
    def configurePlatform(self):
        pass
    
    @abc.abstractmethod
    def startPlatform(self):
        pass
    
    @abc.abstractmethod
    def stopPlatform(self):
        pass
    
    @abc.abstractmethod
    def showPlatforms(self):
        pass




   
