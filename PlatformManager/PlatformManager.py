import sys, os, threading, time, subprocess
from .Platforms.TiddlyWiki import TiddlyWiki

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
    platformProc = None

    #start thread to continue execution 
    def startPlatform(self, start_command):
        print("Initiating Servers")
        thread = threading.Thread(target=self.start, args=(start_command))
        thread.daemon = True
        thread.start()
        return thread
        
    #still under development 
    def configurePlatform(self, main_platform, sub_platforms):
        rint("Creating platforms and integrating them")
        #get list of platforms from plugin manager
        for x in plugin.platforms:
            if(x == main_platform):
                print("Platform Found")
                #instantiate platforms
        for x in sub_platforms:
            print("instantiating subplatforms")

    def start(self, platform):
        platform.processID = subprocess.Popen([platform.get_start_command()], shell=True)
         

    def stop(self, end_command):
        os.system(end_command)
            

#os.system("kill " + str(self.confProc.pid + 1))
platformManager = PlatformManager()
tiddlyWiki = TiddlyWiki()
thread = platformManager.startPlatform(tiddlyWiki)
time.sleep(10)
a = input("Enter a 1 to stop the wiki server: ")
if( a == '1'):
    platformManager.stopPlatform(tiddlywiki.get_end_command)