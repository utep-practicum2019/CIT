import json
from PlatformsManager import PlatformsManager
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

class PlatformInterface():
    cit_IP = "http://127.0.0.1:"
    
    def __init__(self):
        self.platformManager = PlatformsManager()
        
    def parse_JSON(self, json_object):
        with open(json_object, "r") as j_object:
            parsed_input = json.load(j_object)
        
        return parsed_input
    
    def format_request(self, destination, response):
        data = {
                "destination": destination,
                "response": response[0]
                }
        
        json_string = json.dumps(data)
        
        return json_string
    
    ##### Platform Manager #####
    
    def configurePlatform(self, main_platform, subplatforms): #subplatforms is a set
        platform = self.platformManager.createPlatform(main_platform, subplatforms)
        response = False
        
        if (1 <= platform[0] < 100000):
            for x in platform[1]:
                if (1 <= platform[1][x] < 100000):
                    response = True
                    
        return response
    
#     def getPlatformName(platform_ID): 
#         pass
#     
#     def getPlatformID(platform_name): 
#         pass
#     
#     def getPlatformProcessID(platform_ID): 
#         pass
    
    def getSubplatforms(self, platform_ID): 
        pass
    
    def start(self, platform_ID, subplatform_IDs): 
        platform = self.platformManager.startPlatforms(platform_ID, subplatform_IDs)
        response = False
        
        #How can I get the ip:port of a platform if I don't know the name
        
        return response
    
    def stop(self, platform_ID, subplatform_IDs): 
        pass
        
#     def setPlatformName(platform_ID, new_name): 
#         pass

    def removePlatform(self, platform_ID, subplatform_IDs): 
        platform = self.platformManager.deletePlatform(platform_ID, subplatform_IDs)
        
        print(platform)
    
    ##### End Platform Manager #####
    
    ##### Plugin Manager #####
    
    def addPlugin(self, path): 
        pass
    
    def removePlugin(self, plugin_Name): 
        pass
    
    def getAvailablePlugins(self): 
        pass
    
    def getPluginName(self, plugin_ID): 
        pass
    
#     def getPluginID(self, plugin_Name): 
#         pass

    def getPluginStartCommand(self, plugin_Name): 
        pass
    
    def getPluginStopCommand(self, plugin_Name): 
        pass
    
    def getPluginVersion(self, plugin_Name): 
        pass
    
    def getPluginIpPort(self, plugin_Name): 
        pass
    
    def getPluginLink(self, plugin_Name): 
        pass
    
    ##### End Plugin Manager #####
    
p = PlatformsManager()
p_ID, s_IDs = p.createPlatform("Hackathon", {"TiddlyWiki"})
PlatformInterface.removePlatform(p_ID, s_IDs)

     
#print(PlatformInterface.get("Tests/JSON_Test_Files/test.json"))