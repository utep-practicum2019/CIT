import os
import random
import socket
import subprocess
import threading
import time

from .PlatformTreeManager import PlatformTreeManager
# Need to import entire platforms package
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
"""
    Tasks for today:
        * Finish methods for addition, deletion, creating platforms
        * create PlatformTree Manager 
        *if possible test methods    

"""


class PlatformsManager:

    def __init__(self):
        self.PlatformTree = PlatformTreeManager()
        self.plugin_manager = PluginManager()
        self.PlatformTracker = {}

    def createPlatform(self, platform, sub_platforms):
        try:
            available_plugins = self.plugin_manager.getAvailablePlugins()
            print("available plugins" + str(available_plugins))
            if platform not in available_plugins['main_platforms']:
                print("Failure: No Such Plugin: " + platform)
                return "Failure"
            subplatforms = {}
            Main_Platform = self.plugin_manager.loadPlatform(platform)
            for x in sub_platforms:
                if x not in available_plugins['sub_platforms']:
                    print("Failure: No Such Plugin: " + x)
                    return "Failure"
                subplatforms[x] = self.plugin_manager.loadPlatform(x)

            Main_Platform.set_sub_platforms(subplatforms)

            Main_PlatformID, SubplatformIDs = self.PlatformTree.add(Main_Platform)

            return Main_Platform
        except Exception as ex:
            print(ex)
            print("Platform not created. Platform Creation Failed")
            return "Failure"

    def addPlatform(self, platformID, sub_platforms):
        try:
            available_plugins = self.plugin_manager.getAvailablePlugins()
            Main_Platform = self.PlatformTree.getPlatform(platformID)
            if Main_Platform is None:
                print("No such Platform with PlatformID: " + platformID)
                return "Failure"

            subplatforms = Main_Platform.get_sub_platforms()
            sub_platformIDs = {}

            for x in sub_platforms:
                if (x not in available_plugins):
                    print("Failure: No Such Plugin: " + x)
                    return "Failure"
                id = self.PlatformTree.generate_sub_ID(Main_Platform)
                sPlatform = self.plugin_manager.loadPlatform(x)
                sPlatform.setPlatformID(id)
                sub_platformIDs[x] = id
                subplatforms[x] = sPlatform

            return Main_Platform
        except Exception as ex:
            print(ex)
            print("Platform not Added. Platform Creation Failed")
            return "Failure"

    def deletePlatform(self, platformID, subplatformIDs):
        try:
            if subplatformIDs == []:
                Main_Platform = self.PlatformTree.getPlatform(platformID)
                if (Main_Platform is None):
                    print("No such Platform with ID:" + str(platformID))
                    return "Failure"
                self.stopPlatforms(platformID, [])
                self.PlatformTree.remove(platformID)
                return (None, "Success")
            else:
                Main_Platform = self.PlatformTree.getPlatform(platformID)
                if (Main_Platform is None):
                    print("No such Platform with ID:" + str(platformID))
                    return "Failure"
                subPlatforms = Main_Platform.get_sub_platforms()
                for x in list(subPlatforms):
                    if (subPlatforms[x].getPlatformID() in subplatformIDs):
                        if self.check_service(subPlatforms[x]):
                            self.stop(subPlatforms[x])
                        del subPlatforms[x]
                return (Main_Platform, "Success")
        except Exception as ex:
            print(ex)
            print("Platforms Deletion Failed")
            return False

    def getPlatform(self, platformID):
        try:
            Main_Platform = self.PlatformTree.getPlatform(platformID)
            if (Main_Platform is None):
                print("No such Platform with ID: " + str(platformID))
            return Main_Platform
        except Exception as ex:
            print(ex)
            print("Platform not found with ID:" + str(platformID))
            return False

    # This method will start up the specific services
    def startPlatforms(self, platformID, subplatformsIDs):
        try:
            Main_Platform = self.PlatformTree.getPlatform(platformID)
            if (Main_Platform is None):
                print("No such Platform with ID: " + str(platformID))
                return "Failure"

            main_id = Main_Platform.getPlatformID()
            subplatforms = Main_Platform.get_sub_platforms()
            platformTracker = self.PlatformTracker.keys()
            if main_id not in platformTracker:
                if not self.check_service(Main_Platform):
                    self.PlatformTracker[main_id] = []
                    self.startPlatformThread(Main_Platform)
                else:
                    newIP, newPort = self.getPort(Main_Platform)
                    self.PlatformTracker[main_id] = []
                    Main_Platform.setIpPort(newIP, str(newPort))
                    self.startPlatformThread(Main_Platform)
            subTracker = self.PlatformTracker[main_id]
            if subplatformsIDs == []:
                time.sleep(3)
                for x in subplatforms:
                    sub_id = subplatforms[x].getPlatformID()
                    if sub_id not in subTracker:
                        if not self.check_service(subplatforms[x]):
                            subTracker.append(sub_id)
                            self.startPlatformThread(subplatforms[x])
                            time.sleep(3)
                        else:
                            newIP, newPort = self.getPort(subplatforms[x])
                            subplatforms[x].setIpPort(newIP, newPort)
                            subTracker.append(sub_id)
                            self.startPlatformThread(Main_Platform)
                            time.sleep(3)
            else:
                for x in subplatforms:
                    sub_id = subplatforms[x].getPlatformID()
                    if sub_id in subplatformsIDs:
                        sub_id in subplatformsIDs
                        if sub_id not in subTracker:
                            if not self.check_service(subplatforms[x]):
                                subTracker.append(sub_id)
                                self.startPlatformThread(subplatforms[x])
                                time.sleep(3)
                            else:
                                newIP, newPort = self.getPort(subplatforms[x])
                                subTracker.append(sub_id)
                                subplatforms[x].setIpPort(newIP, newPort)
                                self.startPlatformThread(Main_Platform)
                                time.sleep(3)
            return Main_Platform, "Success"
        except Exception as ex:
            print(ex)
            print("Platforms startup failed for Platform" + Main_Platform.getPlatformName() + " " + str(platformID))
            return "Failure"

    # start thread to continue execution
    def startPlatformThread(self, platform):
        try:
            thread = threading.Thread(target=self.start, args=(platform,))
            thread.daemon = True
            thread.start()
            return thread
        except Exception as ex:
            print(ex)
            print("Platform:" + platform.getPlatformName() + " Thread failed")
            return "Failure"

    def start(self, platform):
        try:
            process = subprocess.Popen([platform.get_start_command()], shell=True)
            platform.setProcessID(process.pid + 1)
        except Exception as ex:
            print(ex)
            print("Platform:" + platform.getPlatformName() + " Startup Failed")
            return "Failure"

    def stopPlatforms(self, platformID, subplatformIDs):
        try:
            Main_Platform = self.PlatformTree.getPlatform(platformID)
            if (Main_Platform is None):
                print("No such Platform with ID: " + str(platformID))
                return (None, "Failure")
            subplatforms = Main_Platform.get_sub_platforms()
            platformTracker = self.PlatformTracker.keys()
            if not subplatformIDs:
                for x in subplatforms:
                    if self.check_service(subplatforms[x]):
                        self.stop(subplatforms[x])
                        time.sleep(3)

                if self.check_service(Main_Platform) or platformID in platformTracker:
                    del self.PlatformTracker[platformID]

                    self.stop(Main_Platform)
                    time.sleep(3)
            else:
                subTracker = self.PlatformTracker[platformID]
                for x in subplatforms:
                    subplatformID = subplatforms[x].getPlatformID()
                    if subplatforms[x].getPlatformID() in subplatformIDs:
                        if self.check_service(subplatforms[x]) or subplatformID in subTracker[platformID]:
                            del self.PlatformTracker[platformID][subplatformID]

                            self.stop(subplatforms[x])
                            time.sleep(3)

            return (Main_Platform, "Success")
        except Exception as ex:
            print(ex)
            print("Platform:" + str(platformID) + " Thread failed")
            return (None, "Failure")

    def stop(self, platform):
        try:
            os.system(platform.get_stop_command())
        except Exception as ex:
            print(ex)

    # need to look over this method with team
    def requestForwarder(self, platform, JSON, platform_name):
        response = " "

        if (platform.getPlatformName() == platform_name):
            response = platform.requestHandler(JSON)
        else:
            for x in platform.get_sub_platforms():
                response = platform.subplatform[x].requestHandler(JSON)

        return response

    def checkPlatformStatus(self, platformID, subplatformIDs):
        try:
            serviceUp = True
            main_platform = self.PlatformTree.getPlatform(platformID)
            ServiceStatus = {}
            if (subplatformIDs == []):
                serviceUp = self.check_service(main_platform)
                if (serviceUp == False and not main_platform.staticPlatform):
                    ServiceStatus[main_platform.getPlatformName()] = (main_platform.getPlatformID(), "DOWN")
                else:
                    ServiceStatus[main_platform.getPlatformName()] = (main_platform.getPlatformID(), "UP")
                subps = main_platform.get_sub_platforms()
                for x in subps:
                    serviceUp = self.check_service(subps[x])
                    if (serviceUp or subps[x].staticPlatform):
                        ServiceStatus[subps[x].getPlatformName()] = (subps[x].getPlatformID(), "UP")
                    else:
                        ServiceStatus[subps[x].getPlatformName()] = (subps[x].getPlatformID(), "DOWN")
                return ServiceStatus
            else:
                serviceUp = self.check_service(main_platform)
                if (serviceUp == False and not main_platform.staticPlatform):
                    ServiceStatus[main_platform.getPlatformName()] = (main_platform.getPlatformID(), "DOWN")
                else:
                    ServiceStatus[main_platform.getPlatformName()] = (main_platform.getPlatformID(), "UP")
                subps = main_platform.get_sub_platforms()
                for x in subps:
                    if (subps[x].getPlatformID() in subplatformIDs):
                        serviceUp = self.check_service(subps[x])
                        if (serviceUp or subps[x].staticPlatform):
                            ServiceStatus[subps[x].getPlatformName()] = (subps[x].getPlatformID(), "UP")
                        else:
                            ServiceStatus[subps[x].getPlatformName()] = (subps[x].getPlatformID(), "Down")
                return ServiceStatus
        except Exception as ex:
            print(ex)
            return "Failure"

    def check_service(self, platform):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = platform.getIpPort()
        ip, port = address.split(":")
        port = int(port)
        # print(ip + str(port))
        try:
            s.connect((ip, port))
            s.close()
            return True
        except:
            return False

    def check_IPport(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            s.close()
            return True
        except:
            return False

    def getPort(self, platform):
        IPport = platform.getIpPort()
        ip, port = IPport.split(":")
        randPort = random.randint(10000, 65000)
        while (self.check_IPport(ip, randPort)):
            randPort = random.randint(1, 65000)
        return (ip, randPort)

    def printPlatforms(self, platformid):
        main_platform = self.PlatformTree.getPlatform(platformid)
        print("Main Platform: " + main_platform.getPlatformName() + " id: " + str(main_platform.getPlatformID()))
        print("Subplatforms: ")
        subplatforms = main_platform.get_sub_platforms()
        for x in subplatforms:
            print("         " + subplatforms[x].getPlatformName() + " id: " + str(subplatforms[x].getPlatformID()))

# A = PlatformsManager()
# Main_Platform = A.createPlatform("FilesUpload", ["Rocketchat", "TiddlyWiki"])
# MainID = Main_Platform.getPlatformID()
# Main_Platform.requestHandler({"command":"addFile", "parameters": {"filePath": "./Platforms/Read/Albert.txt"}})
# Main_Platform.requestHandler({"command":"delFile", "parameters": {"file": "Albert.txt"}})
# # sub_platforms = Main_Platform.get_sub_platforms()
# # subIDs = []
# # for x in sub_platforms:
# #     subIDs.append(sub_platforms[x].getPlatformID())
# # C = A.startPlatforms(MainID, subIDs)
# # input("whenever bruh")
# # status = A.checkPlatformStatus(MainID, [])
# # B = A.addPlatform(MainID, {"TiddlyWiki"})
# # C = A.startPlatforms(MainID, [])
# # input("whenever bruh")
# # status = A.checkPlatformStatus(MainID, [])
# # print("status" + str(status))
# # input("whenever bruh")
# # time.sleep(5)
# A.stopPlatforms(MainID, [] )
# input("whenever bruh")
