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
        
#     def parse_JSON(self, json_object):
#         with open(json_object, "r") as j_object:
#             parsed_input = json.load(j_object)
#         
#         return parsed_input
#     
#     def format_request(self, destination, request):
#         data = {
#                 "destination": destination,
#                 "request": request[0]
#                 }
#         
#         json_string = json.dumps(data)
#         
#         return json_string
    
    ##### Platform Manager #####
    
    def createPlatform(self, main_platform, subplatforms): #subplatforms is a set
        Main_Platform = self.platformManager.createPlatform(main_platform, subplatforms)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        
        response = False
        
        if (1 <= Main_Platform.getPlatformID() < 100000):
            for x in range(0, len(sub_keys)):
                
                print(Subplatforms[sub_keys[x]].getPlatformID())###TEST(Remove)###
                
                if (1 <= Subplatforms[sub_keys[x]].getPlatformID() < 100000):
                    response = True
                    
        return {response}
     
    def deletePlatform(self, platform_ID, subplatform_IDs): 
        Main_Platform = self.platformManager.deletePlatform(platform_ID, subplatform_IDs)
        
        if (subplatform_IDs != { }):
            response = {Main_Platform[1], Main_Platform[0].getPlatformID()}
            
        else:
            response = {Main_Platform[1]}
                    
        return response
    
    def addPlatform(self, platform_ID, subplatforms): 
        Main_Platform = self.platformManager.addPlatform(platform_ID, subplatforms)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        
        response = False
        
        if (1 <= Main_Platform.getPlatformID() < 100000):
            for x in range(0, len(sub_keys)):
                
                print(Subplatforms[sub_keys[x]].getPlatformID())###TEST(Remove)###
                
                if (1 <= Subplatforms[sub_keys[x]].getPlatformID() < 100000):
                    response = True
                    
        return {response}
    
    def startPlatform(self, platform_ID, subplatform_IDs): 
        Main_Platform = self.platformManager.startPlatforms(platform_ID, subplatform_IDs)
        subplatforms = Main_Platform[0].get_sub_platforms()
        response = set()
        
        if (subplatform_IDs != { }):
            for x in subplatforms:
                response.add(subplatforms[x].getIpPort())
            
        response.add(Main_Platform[0].getIpPort())
            
        return response
    
    def stopPlatform(self, platform_ID, subplatform_IDs): 
        status = self.platformManager.stopPlatforms(platform_ID, subplatform_IDs)
        
        return status
    
    ##### End Platform Manager #####
    
    ##### Plugin Manager #####
    
    def addPlugin(self, path): 
        pass
    
    def deletePlugin(self, plugin_Name): 
        pass
    
    def getAvailablePlugins(self): 
        pass
    
    def loadPlatform(self):
        pass
    
    ##### End Plugin Manager #####
    
    def test(self):
        ###################### TEST: deletePlatform ##############################
#         main_p = self.platformManager.createPlatform("Hackathon", {"TiddlyWiki"})
#         print(main_p)
#          
#         print(self.deletePlatform(main_p.getPlatformID(), main_p.get_sub_platforms()))
        ##########################################################################
        
        #################### TEST: deletePlatform(no subs) #######################
#         main_p = self.platformManager.createPlatform("Hackathon", {})
#         print(main_p)
#           
#         print(self.deletePlatform(main_p.getPlatformID(), {}))
        ##########################################################################
        
        ########################## TEST: addPlatform #############################
#         main_p = self.platformManager.createPlatform("Hackathon", {})
#         print(self.addPlatform(main_p.getPlatformID(), {"TiddlyWiki"}))
#         
#         #print(self.deletePlatform(main_p.getPlatformID(), {}))
        ##########################################################################
        
        ################### TEST: startPlatform/stopPlatform #####################
        main_p = self.platformManager.createPlatform("Hackathon", {})
        print(self.startPlatform(main_p.getPlatformID(), {}))
        
        print(self.stopPlatform(main_p.getPlatformID(), {}))
         
        #print(self.deletePlatform(main_p.getPlatformID(), {}))
        ##########################################################################
        
                
pi = PlatformInterface()
pi.test()
#print(main_p)
# print(main_p.getIpPort())
#print(type(main_p.getPlatformID()))
# sub_p = main_p.get_sub_platforms()
# sub_keys = list(sub_p.keys())
# print(sub_keys[0])
# print("Platform ID: "+ str(sub_p[sub_keys[0]].getPlatformID()))

# ###Test createPlatform###
# pi = PlatformInterface()
# print(pi.createPlatform("Hackathon", {"TiddlyWiki"}))
     
#print(PlatformInterface.get("Tests/JSON_Test_Files/test.json"))