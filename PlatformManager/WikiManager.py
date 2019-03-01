import sys
import os
#from yapsy.PluginManager import PluginManager
import abc
from PlatformsManager import PlatformManager

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class WikiManager(PlatformManager):

    def configurePlatform(self):
        print("configuring service")

    def startPlatform(self):
        print("starting platform wiki")
        os.system("tiddlywiki editions/tw5.com-server --listen ")

    def stopPlatform(self):
        print("stopping a service")



platformManager = WikiManager()
platformManager.startPlatform()
platformManager.stopPlatform()
