import sys, os, threading, time, subprocess, socket
#Need to import entire platforms package
from PluginManager import PluginManager

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

    def startPlatforms(self, platform):
        self.startPlatformThread(platform)
        time.sleep(3)
        for x in platform.subplatforms:
            self.startPlatformThread(platform.subplatforms[x])
            time.sleep(3)

    #start thread to continue execution 
    def startPlatformThread(self, platform):
        print("Initiating Servers")
        thread = threading.Thread(target=self.start, args=(platform, ))
        thread.daemon = True
        thread.start()
        return thread
        
    #still under development 
    def configurePlatform(self, main_platform, sub_platforms):
        subplatforms = {}
        plugin_manager = PluginManager()
        Main_Platform = plugin_manager.loadPlatform(main_platform)
        for x in sub_platforms:
            subplatforms[x] = plugin_manager.loadPlatform(x)
        Main_Platform.set_sub_platforms(subplatforms)
        return Main_Platform

    def start(self, platform):
        process = subprocess.Popen([platform.get_start_command()], shell=True)
        print("process id: " + str(process.pid))
        platform.setProcessID(process.pid + 1)
        print("Platform Process ID " + str(platform.getProcessID()))

    def stopPlatforms(self, platform, platforms):
        if(platform.getPlatformName() in platforms):
            for x in platform.subplatforms:
                self.stop(platform.subplatforms[x])
                time.sleep(3)
            self.stop(platform)
            time.sleep(3)
        else:
            for x in platform.subplatforms:
                if(platform.subplatforms[x].getPlatformName in platforms):
                    self.stop(platform.subplatforms[x])
        return "Success"
        
        
    def stop(self, platform):
        print("Platform Process ID: " + str(platform.getProcessID()))
        os.system(platform.get_stop_command())
    
    ''' NEED TO CHECK IF SERVICES ARE RUNNING 
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
    '''
    def requestForwarder(self, platform, JSON, platform_name):
        response = " "
        if(platform.getPlatformName() == platform_name):
            response = platform.requestHandler(JSON)
        else:
            for x in platform.get_sub_platforms():
                response = platform.subplatform[x].requestHandler(JSON)
        return response


        
        
        
            


platformManager = PlatformsManager()
wiki = platformManager.configurePlatform("TiddlyWiki", {"RocketChat"})
platformManager.startPlatforms(wiki)

a = input("Enter a 1 to stop the wiki server: ")
if( a == '1'):
    platformManager.stopPlatforms(wiki, {})
