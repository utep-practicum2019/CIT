import sys, os, threading, time, subprocess, socket
#Need to import entire platforms package
from .Platforms.TiddlyWiki import TiddlyWiki
from .Platforms.RocketChat import RocketChat

from .PluginManager import PluginManager

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """
'''
    Tasks for today:
        *Think of fields needed for Platform Manager
        *Start up RocketChat

        If possible: 
            Start up both wiki and rocketchat

'''
class PlatformsManager:
    PlatformManagerID = 0
    Main_Platform = None
    

    #start thread to continue execution 
    def startPlatformThread(self, platform):
        print("Initiating Servers")
        thread = threading.Thread(target=self.start, args=(platform, ))
        thread.daemon = True
        thread.start()
        return thread
        
    #still under development 
    def configurePlatform(self, main_platform, sub_platforms):
        print("Creating platforms and integrating them")
        #get list of platforms from plugin manager
        

    def start(self, platform):
        process = subprocess.Popen([platform.get_start_command()], shell=True)
        print("process id: " + str(process.pid))
        platform.setProcessID(process.pid + 1)
        print("Platform Process ID " + str(platform.getProcessID()))
        
        
    def stop(self, platform):
        print("Platform Process ID: " + str(platform.getProcessID()))
        os.system(platform.get_stop_command())
    
    #need to figure out if service is running on ip and port 
    def serviceIsRunning(self, platform):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip, port = platform.getIpPort().split(":")
        print(ip + " " + port)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return "200"
        except:
            return "404"
        
        
        
            


platformManager = PlatformsManager()
tiddlywiki = TiddlyWiki()
rocketChat = RocketChat()
thread = platformManager.startPlatformThread(rocketChat)
time.sleep(10)
thread = platformManager.startPlatformThread(tiddlywiki)
time.sleep(10)
a = input("Enter a 1 to stop the wiki server: ")
if( a == '1'):
    platformManager.stop(rocketChat)
    time.sleep(10)
    platformManager.stop(tiddlywiki)