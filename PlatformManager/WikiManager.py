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
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class WikiManager(PlatformManager):
    paltformProc = 0
    confProc = 0
    def __init__(self):
        print("Initializing Wiki")

    def startPlatform(self):
        print("Initiating wiki Server")
        thread = threading.Thread(target=self.startWiki, args=())
        thread.daemon = True
        thread.start()
        return thread
        
        
    def configurePlatform(self):
        print("Initiating Tiddly Wiki Server")
        thread = threading.Thread(target=self.configureWiki, args=())
        thread.daemon = True
        thread.start()
        return thread

    def configureWiki(self):
        self.confProc = subprocess.Popen([ "tiddlywiki /home/practicum/Documents/tiddlywikis/genericWiki  --listen port=8084 host=0.0.0.0"], shell=True)
        

    def startWiki(self):
        self.platformProc = subprocess.Popen([ "http-server -a 0.0.0.0 -p 8085"], shell=True)
         

    def stopPlatform(self):
        print("stopping a service")
        if(self.platformProc.pid):
            os.system("kill " + str(self.platformProc.pid + 1))
        if(self.confProc):
            os.system("kill " + str(self.confProc.pid + 1))

platformManager = WikiManager()
thread = platformManager.startPlatform()
time.sleep(10)
a = input("Enter a 1 to stop the wiki server: ")
if( a == '1'):
    platformManager.stopPlatform()

