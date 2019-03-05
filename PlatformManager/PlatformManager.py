import sys
import os
import threading
import abc
import time
import subprocess

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class PlatformManager:
    PlatformManagerID = 0
    Main_Platform = None
    threads = {}

    def startPlatform(self, main_platform, subplatforms):
        print("Initiating Servers")
        thread = threading.Thread(target=self.start, args=())
        thread.daemon = True
        thread.start()
        return thread
        
        
    def configurePlatform(self, main_platform, sub_platforms):
        print("Creating platforms and integrating them")
        #get list of platforms from plugin manager
        for x in plugin.platforms:
            if(x == main_platform):
                print("Platform Found")
                #instantiate platforms
        for x in sub_platforms:
            print("instantiating subplatforms")

    def startWiki(self, start_command):
        self.platformProc = subprocess.Popen([start_command], shell=True)
         

    def stopPlatform(self, end_command):
        os.system(end_command)
            

#os.system("kill " + str(self.confProc.pid + 1))
platformManager = PlatformManager()
thread = platformManager.startPlatform()
time.sleep(10)
a = input("Enter a 1 to stop the wiki server: ")
if( a == '1'):
    platformManager.stopPlatform()