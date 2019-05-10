import datetime
import os
import random
import requests
import socket
import subprocess
import threading
import time
import atexit


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
        self.CITURL = os.environ.get('HOST')
        #self.CITURL = 'http://127.0.0.1:5001'
        self.PlatformsURL = "/api/v2/resources/platform?all=True"
        self.getPlatformsURL = self.CITURL + self.PlatformsURL
        self.reinstantiated = False
        self.reinstantiateThread()

        def closePlatforms():
            root = self.PlatformTree.getRoot()
            closingPlatforms(root)

        def closingPlatforms(node):
            if (node == None):
                return
            else:
                self.stopPlatforms(node.platformID, [])
                closingPlatforms(node.rightNode)
                closingPlatforms(node.leftNode)

        atexit.register(closePlatforms)



    def reinstantiateThread(self):
        try:
            thread = threading.Thread(target=self.reinstantiate, args=())
            thread.daemon = True
            thread.start()
            return
        except Exception as ex:
            print(ex)
            return "Failure"

    def reinstantiate(self):
        time.sleep(1)
        response = requests.get(self.getPlatformsURL)
        # print("RESPONSE " + str(response.json()))
        platformList = response.json()
        for x in range(0, len(platformList)):
            # response[x] platform number x
            resp = platformList[x]
            Main_Platform = self.plugin_manager.loadPlatform(resp["main"]["name"])
            Main_Platform.setPlatformID(int(resp["main"]["id"]))
            ip, port = resp["main"]["ip_port"].split(":")
            Main_Platform.setIpPort(ip, port)
            Main_Platform.setPlatformAlias(resp["main"]["alias"])
            Main_Platform.setPlatformNote(resp["main"]["note"])
            subs = {}
            for x in range(0, len(resp["subplatforms"])):
                subplatform = resp["subplatforms"][x]
                subPlatform = self.plugin_manager.loadPlatform(subplatform["name"])
                subPlatform.setPlatformID(subplatform["id"])
                ip, port = subplatform["ip_port"].split(":")
                subPlatform.setIpPort(ip, port)
                Main_Platform.setPlatformAlias(subplatform["alias"])
                Main_Platform.setPlatformNote(subplatform["note"])
                subs[subPlatform.getPlatformName()] = subPlatform
            Main_Platform.set_sub_platforms(subs)
            self.PlatformTree.reAdd(Main_Platform)
            # print("Main Platform: " + Main_Platform.getPlatformName() + " subplatforms: " + str(
            # Main_Platform.get_sub_platforms()))




    def createPlatform(self, platform, sub_platforms):
        try:
            available_plugins = self.plugin_manager.getAvailablePlugins()
            # print("available plugins" + str(available_plugins))
            if platform not in available_plugins['main_platforms']:
                print("Failure: No Such Plugin: " + platform)
                return "Failure"
            subplatforms = {}
            Main_Platform = self.plugin_manager.loadPlatform(platform)

            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Main_Platform.setPlatformDateCreated(date)

            for x in sub_platforms:
                if x not in available_plugins['sub_platforms']:
                    print("Failure: No Such Plugin: " + x)
                    return "Failure"
                subplatforms[x] = self.plugin_manager.loadPlatform(x)
                # date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # subplatforms[x].setPlatformDateCreated(date)

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
                if (x not in available_plugins["sub_platforms"]):
                    print("Failure: No Such Plugin: " + x)
                    return "Failure"
                id = self.PlatformTree.generate_sub_ID(Main_Platform)
                sPlatform = self.plugin_manager.loadPlatform(x)
                sPlatform.setPlatformID(id)

                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sPlatform.setPlatformDateCreated(date)

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
            # checking if platform is not already running
            if main_id not in platformTracker:
                # check if platform IP is available, if not re assign IP
                if not self.check_service(Main_Platform):
                    self.PlatformTracker[main_id] = []
                    self.start(Main_Platform)
                else:
                    newIP, newPort = self.getPort(Main_Platform)
                    self.PlatformTracker[main_id] = []
                    Main_Platform.setIpPort(newIP, str(newPort))
                    self.start(Main_Platform)
            subTracker = self.PlatformTracker[main_id]
            # instantiate all subplatforms if it is an empty list
            if subplatformsIDs == []:
                time.sleep(3)
                for x in subplatforms:
                    sub_id = subplatforms[x].getPlatformID()
                    if sub_id not in subTracker:
                        if not self.check_service(subplatforms[x]):
                            subTracker.append(sub_id)
                            self.start(subplatforms[x])
                            time.sleep(3)
                        else:
                            newIP, newPort = self.getPort(subplatforms[x])
                            subplatforms[x].setIpPort(newIP, newPort)
                            subTracker.append(sub_id)
                            self.start(Main_Platform)
                            time.sleep(3)
            else:  # Instantiate Specific Platforms
                for x in subplatforms:
                    sub_id = subplatforms[x].getPlatformID()
                    if sub_id in subplatformsIDs:
                        sub_id in subplatformsIDs
                        if sub_id not in subTracker:
                            if not self.check_service(subplatforms[x]):
                                subTracker.append(sub_id)
                                self.start(subplatforms[x])
                                time.sleep(3)
                            else:
                                newIP, newPort = self.getPort(subplatforms[x])
                                subTracker.append(sub_id)
                                subplatforms[x].setIpPort(newIP, newPort)
                                self.start(Main_Platform)
                                time.sleep(3)
            return Main_Platform, "Success"
        except Exception as ex:
            print(ex)
            print("Platforms startup failed for Platform" + Main_Platform.getPlatformName() + " " + str(platformID))
            return "Failure"

    def start(self, platform):
        try:
            # keep track of processID
            process = subprocess.Popen([platform.get_start_command()], shell=True)
            # any other processes that are executed in child process is process id + the number of extra processes.
            # Since specific platforms produce an extra thread under the child process, the process ID for that platform is child process id + 1
            platform.setProcessID(process.pid + 1)
        except Exception as ex:
            print(ex)
            print("Platform:" + platform.getPlatformName() + " Startup Failed")
            return "Failure"

    def stopPlatforms(self, platformID, subplatformIDs):
        # try:
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
            # print(str(subTracker))
            for x in subplatforms:
                subplatformID = subplatforms[x].getPlatformID()
                if subplatforms[x].getPlatformID() in subplatformIDs:
                    if self.check_service(subplatforms[x]) or subplatformID in subTracker:
                        indx = subTracker.index(subplatformID)
                        del self.PlatformTracker[platformID][indx]

                        self.stop(subplatforms[x])
                        time.sleep(3)

        return (Main_Platform, "Success")
        '''
    except Exception as ex:
        print(ex)
        print("Platform:" + str(platformID) + " Thread failed")
        return (None, "Failure")
        '''

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
# a = input()
# A.startPlatforms(8000, [])
# a = input()
# A.stopPlatforms(8000, [9090])
# a = input()
# A.stopPlatforms(8000,[])
