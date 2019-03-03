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
            The plugin manager will be able to start, stop, restart, and configure Chat platform.
    """

class ChatManager(PlatformManager):

        def configurePlatform(self):
            print("configuring a chat service")

        def startPlatform(self):
            print("starting a Chat service")
            os.system("service snap.rocketchat-server.rocketchat-server start")

        def stopPlatform(self):
            print("stopping a chat service")
            os.system("service snap.rocketchat-server.rocketchat-server stop")

        def restartPlatform(self):
            print("restarting a chat service")
            os.system("service snap.rocketchat-server.rocketchat-server restart")


platformManager = ChatManager()
platformManager.configurePlatform()
platformManager.startPlatform()
platformManager.stopPlatform()
platformManager.restartPlatform()