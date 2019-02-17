import sys
import os 
from yapsy.PluginManager import PluginManager
import abc
from .PlatformsManager import PlatformManager

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes

        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class SubmissionManager(PlatformManager):
    
    def addPlatform(self):
        print("adding plugin")
    
    def removePlatform(self):
        print("removing plugin")

    def configurePlatform(self):
        print("configuring service")
    
    
    def startPlatform(self):
        print("starting a service")
    
    
    def stopPlatform(self):
        print("stopping a service")
    
    
    def showPlatforms(self):
        print("showing services")


platfromManager =SubmissionManager()
platfromManager.addPlatform()
platfromManager.removePlatform()
platfromManager.configurePlatform()
platfromManager.showPlatforms()
platfromManager.startPlatform()
platfromManager.stopPlatform()
