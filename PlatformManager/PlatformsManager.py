import sys, os, threading, time, subprocess, socket, random 
#Need to import entire platforms package
from PluginManager import PluginManager
from PlatformTreeManager import PlatformTreeManager

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
"""
"""
    Tasks for today:
        * Finish methods for addition, deletion, creating platforms
        * create PlatformTree Manager 
        *if possible test methods    

"""
class PlatformsManager:
    def __init__(self):
        self.PlatformTree = PlatformTreeManager()
       

    # argument takes string and list of strings
    def createPlatform(self, platform, sub_platforms):
        subplatforms = {}
        plugin_manager = PluginManager()
        Main_Platform = plugin_manager.loadPlatform(platform)
        for x in sub_platforms:
            subplatforms[x] = plugin_manager.loadPlatform(x)
        Main_Platform.set_sub_platforms(subplatforms)
        Main_PlatformID, SubplatformIDs = self.PlatformTree.add(Main_Platform)
        return (Main_PlatformID, SubplatformIDs)
    
    #argument takes a string id and a list of strings of ID's
    #implement some try and catches
    def addPlatform(self, platformID, sub_platforms):
        plugin_manager = PluginManager()
        Main_Platform = self.PlatformTree.getPlatform(platformID)
        subplatforms = Main_Platform.get_sub_platforms()
        sub_platformIDs = {}
        for x in sub_platforms:
            """
                Need to generate IDS in a more unique way lol 
            """
            id = random.randint(1, 100000)
            sPlatform = plugin_manager.loadPlatform(x)
            sPlatform.setPlatformID(id)
            #sub_platformIDs.add(sPlatform.getPlatformID())
            subplatforms[x] = sPlatform
        return (Main_Platform.getPlatformID(), sub_platformIDs)
    
    def deletePlatform(self, platformID, subplatformIdentifiers):
        #removing a platform will consist of stopping a platform and then removing the instance 
        if(subplatformIdentifiers == { }):
            Main_Platform = self.PlatformTree.Remove(platformID)
            return (platformID, "success")
        else:
            Main_Platform = self.PlatformTree.getPlatform(platformID)
            subPlatforms = Main_Platform.get_sub_platforms()
            for x in subPlatforms:
                if(x in subPlatforms):
                    del 
            return (platformID, "success")
            

    #This method will start up the specific services
    def startPlatforms(self, platform, platforms):
        #implement logic to start up specific services
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

    def start(self, platform):
        process = subprocess.Popen([platform.get_start_command()], shell=True)
        print("process id: " + str(process.pid))
        platform.setProcessID(process.pid + 1)
        print("Platform Process ID " + str(platform.getProcessID()))
        
    #still under development 
    '''
        Need to add logic to manually remove a platform from an object or instantiate a platform
        given the set of platforms
    '''

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

    def requestForwarder(self, platform, JSON, platform_name):
        response = " "
        if(platform.getPlatformName() == platform_name):
            response = platform.requestHandler(JSON)
        else:
            for x in platform.get_sub_platforms():
                response = platform.subplatform[x].requestHandler(JSON)
        return response
    def printPlatforms(self, platformid):
        main_platform = self.PlatformTree.getPlatform(platformid)
        print("Main Platform:" + main_platform.getPlatformName())
        print("Subplatforms: ")
        subplatforms = main_platform.get_sub_platforms()
        for x in subplatforms:
            print("         " + subplatforms[x].getPlatformName())

platformsManager = PlatformsManager()
wikiID, WikiSubIDs = platformsManager.createPlatform("TiddlyWiki", {"RocketChat", "Submission", "Hackathon"})
chatID, WikiSubIDs = platformsManager.createPlatform("RocketChat", {"TiddlyWiki", "Submission"})
hackathonID, HackSubIDs = platformsManager.createPlatform("Submission", {"RocketChat", "RocketChat", "Hackathon"})
RapidCyberID, HackSubIDs = platformsManager.createPlatform("RapidCyber", {"TiddlyWiki", "Submission"})



print("Printing Tree")
platformTree = platformsManager.PlatformTree
platformTree.printTree(platformTree.root)
print("Printing Wiki")
platformsManager.printPlatforms(wikiID)
platformsManager.printPlatforms(chatID)

platformsManager.addPlatform(wikiID, {"RapidCyber"})

print("Printing updated Wiki")
platformsManager.printPlatforms(wikiID)

