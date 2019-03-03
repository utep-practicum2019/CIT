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
    proc = 0
    def __init__(self):
        print("Initializing Wiki Class")
        
    def startPlatform(self):
        print("Initiating Tiddly Wiki Server")
        thread = threading.Thread(target=self.startWiki, args=())
        thread.daemon = True
        thread.start()
        return thread

    def configurePlatform(self):
        print("configuring service")

    def startWiki(self):
        print("starting platform wiki")
        self.proc = subprocess.Popen([ "tiddlywiki /home/practicum/Documents/tiddlywikis/genericWiki --listen port=8081 --load /home/practicum/Documents/tiddlywikis/genericWiki/arl.html"], shell=True)
        print("procees id " + str(self.proc))
        

    def stopPlatform(self):
        print("stopping a service")
        os.system("kill " + str(self.proc.pid + 1))

platformManager = WikiManager()
thread = platformManager.startPlatform()
time.sleep(10)
a = input("Enter a 1 to stop the tiddles: ")

if( a == '1'):
    platformManager.stopPlatform()

