import sys, os, threading, time, subprocess, socket, random 
#Need to import entire platforms package
from PluginManager import PluginManager
from PlatformTreeManager import PlatformTreeManager, PlatformTree

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
        
        return Main_Platform
    
    #argument takes a string id and a list of strings of ID's
    #implement some try and catches
    def addPlatform(self, platformID, sub_platforms):
        plugin_manager = PluginManager()
        Main_Platform = self.PlatformTree.getPlatform(platformID)
        subplatforms = Main_Platform.get_sub_platforms()
        sub_platformIDs = {}
        
        for x in sub_platforms:
            id = self.PlatformTree.generate_sub_ID(Main_Platform)
            sPlatform = plugin_manager.loadPlatform(x)
            sPlatform.setPlatformID(id)
            sub_platformIDs[x] = id 
            subplatforms[x] = sPlatform
        
        return Main_Platform
    
    def deletePlatform(self, platformID, subplatformIDs):
        #removing a platform will consist of stopping a platform and then removing the instance 
#         print (type(platformID))
#         print(subplatformIDs)
        print(self.PlatformTree.printTree(self.PlatformTree.getRoot()))
        if(subplatformIDs == { }):
            Main_Platform = self.PlatformTree.remove(platformID)
            return (None, "Success")
        else:
            Main_Platform = self.PlatformTree.getPlatform(platformID)
            subPlatforms = Main_Platform.get_sub_platforms()
            for x in list(subPlatforms):
                if(subPlatforms[x].getPlatformID() in subplatformIDs):
                    del subPlatforms[x] 
            return (Main_Platform, "Success")
            
    def getPlatform(self, platformID):
        Main_Platform = self.PlatformTree.getPlatform(platformID)

        return Main_Platform

        
    #This method will start up the specific services
    def startPlatforms(self, platformID, subplatformsIDs):
        Main_Platform = self.PlatformTree.getPlatform(platformID)
        subplatforms = Main_Platform.get_sub_platforms()
        self.startPlatformThread(Main_Platform)
        
        if(subplatformsIDs == { }):
            time.sleep(3)
            for x in subplatforms:
                self.startPlatformThread(subplatforms[x])
                time.sleep(3)
        else:
            for x in subplatforms:
                if(subplatforms[x].getPlatformID() in subplatformsIDs):
                    self.startPlatformThread(subplatforms[x])
        return (Main_Platform, "Success")


    #start thread to continue execution 
    def startPlatformThread(self, platform):
        print("Initiating Servers")
        
        thread = threading.Thread(target=self.start, args=(platform, ))
        thread.daemon = True
        thread.start()
        
        return thread

    def start(self, platform):
        process = subprocess.Popen([platform.get_start_command()], shell=True)
        platform.setProcessID(process.pid + 1)

    def stopPlatforms(self, platformID, subplatformIDs):
        Main_Platform = self.PlatformTree.getPlatform(platformID)
        subplatforms = Main_Platform.get_sub_platforms()
        
        if(subplatformIDs == {}):
            for x in subplatforms:
                self.stop(subplatforms[x])
                time.sleep(3)
            self.stop(Main_Platform)
            time.sleep(3)
        else:
            for x in subplatforms:
                if(subplatforms[x].getPlatformID() in subplatformIDs):
                    self.stop(subplatforms[x])
        
        return "Success"
           
    def stop(self, platform):
        print("Platform Process ID: " + str(platform.getProcessID()))
        
        os.system(platform.get_stop_command())

    #need to look over this method with team 
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
        
        print("Main Platform: " + main_platform.getPlatformName() + " id: " + str(main_platform.getPlatformID()))
        print("Subplatforms: ")
        
        subplatforms = main_platform.get_sub_platforms()
        
        for x in subplatforms:
            print("         " + subplatforms[x].getPlatformName()+ " id: " + str(subplatforms[x].getPlatformID()))
# 
# platformsManager = PlatformsManager()
# hackID, hackSubIDs = platformsManager.createPlatform("Hackathon", {"TiddlyWiki", "RocketChat"})
# platformsManager.printPlatforms(hackID)
# hackID, wikiSubIds = platformsManager.addPlatform(hackID, {"Submission"})
# platformsManager.printPlatforms(hackID)
# wikiID = hackSubIDs["TiddlyWiki"]
# chatID = hackSubIDs["RocketChat"]
# #platformsManager.deletePlatform(hackID, {wikiID}) 
# platformsManager.printPlatforms(hackID)
# 
# platformsManager.startPlatforms(hackID, { })
# time.sleep(10)
# 
# running = True
# while(running):
#     try:
#         a = input()
#         if(int(a) == 1):
#             platformsManager.stopPlatforms(hackID, {} )
#         elif(int(a) == 2):
#             platformsManager.startPlatforms(hackID, {wikiID})
#         else:
#             running = False
#     except NameError:
#         pass


