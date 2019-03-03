import sys
import os
import threading
import abc
import time
import subprocess

from PlatformsManager import PlatformManager

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to start, stop, and configure Chat platform.
    """

class ChatManager(PlatformManager):
    proc = 0
    def __init__(self):
            print("Initializing Chat Class")

    def startPlatform(self):
            print("Initiating Chat Server")
            thread = threading.Thread(target=self.startChat, args=())
            thread.daemon = True
            thread.start()
            return thread

     def configurePlatform(self):
            print("Configuring a chat service")

    def startChat(self):
            print("Starting Chat platform")
            self.proc = subprocess.Popen(["service snap.rocketchat-server.rocketchat-server start"], shell=True)
            print("procees id " + str(self.proc))

    def stopPlatform(self):
            print("stopping a chat service")
            os.system("kill " + str(self.proc.pid + 1))


platformManager = ChatManager()
thread = platformManager.startPlatform()
time.sleep(10)
a = input("Enter 1 to stop the Chat platform: ")

if( a == '1'):
    platformManager.stopPlatform()
