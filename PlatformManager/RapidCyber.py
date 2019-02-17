import sys
import os
from yapsy.PluginManager import PluginManager
import abc
from .PlatformManager import PlatformManager

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class RapidCyber(PlatformManager):

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


platformManager = PlatformManager()
platformManager.addPlatform()
platformManager.removePlatform()
platformManager.configurePlatform()
platformManager.showPlatforms()
platformManager.startPlatform()
platformManager.stopPlatform()