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
        Subplatforms = Main_Platform[0].get_sub_platforms()
        response = set()
        
        if (subplatform_IDs != { }):
            for x in Subplatforms:
                response.add(Subplatforms[x].getIpPort())
            
        response.add(Main_Platform[0].getIpPort())
            
        return response
    
    def stopPlatform(self, platform_ID, subplatform_IDs): 
        status = self.platformManager.stopPlatforms(platform_ID, subplatform_IDs)
        
        return status


    def getPlatform(self, platform_ID, subplatform_IDs): 
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform[0].get_sub_platforms()
        response = {}
        info = []
        info.append({"name" : Main_Platform.getPlatformName(),
                    "ip:port" : Main_Platform.getIPPort()})

        if (subplatform_IDs != { }):
            for x in Subplatforms:
                info.append({"name" : subplatform_IDs[x].getPlatformName(),
                            "ip:port" : subplatform_IDs[x].getIpPort()})

        response = {info}
                    
        return response
    
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

    ##### Rocket Chat #####
    
    def rocketChatRegisterUser(self, platform_ID, subPlatform_ID, user_email, username, user_pass, user_nick):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())

        if (Main_Platform.getPlatformID == platform_ID):
            status, userID = Main_Platform.registerUser(user_email, username, user_pass, user_nick)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, userID = Subplatforms[sub_keys[x]].registerUser(user_email, username, user_pass, user_nick)

        print(status)
        print(userID)
                
    
    def rocketChatLoginUser(self, platform_ID, subPlatform_ID, username, user_pass):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())

        if (Main_Platform.getPlatformID == platform_ID):
            status, authToken = Main_Platform.loginUser(username, user_pass)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, authToken = Subplatforms[sub_keys[x]].loginUser(username, user_pass)

        print(status)
        print(authToken)
    
    def rocketChatGetUserInfo(self, platform_ID, subPlatform_ID, user_ID, username): 
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())

        if (Main_Platform.getPlatformID == platform_ID):
            status, userID, email, userName, userNick = Main_Platform.getUserInfo(user_ID, username)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, userID, email, userName, userNick = Subplatforms[sub_keys[x]].getUserInfo(user_ID, username)

        print(status)
        print(userID)
        print(email)
        print(userName)
        print(userNick)
    
    def rocketChatDeleteUser(self, platform_ID, subPlatform_ID, user_ID):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())

        if (Main_Platform.getPlatformID == platform_ID):
            status = Main_Platform.deleteUser(user_ID)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status = Subplatforms[sub_keys[x]].deleteUser(user_ID)
        print(status)

    def rocketChatCreateChannel(self, platform_ID, subPlatform_ID, channel_name):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())

        if (Main_Platform.getPlatformID == platform_ID):
            status, roomID = Main_Platform.createChannel(channel_name)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, roomID = Subplatforms[sub_keys[x]].createChannel(channel_name)
        
        print(status)
        print(roomID)

    def rocketChatDeleteChannel(self, platform_ID, subPlatform_ID, room_ID):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())

        if (Main_Platform.getPlatformID == platform_ID):
            status = Main_Platform.deleteChannel(room_ID)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status = Subplatforms[sub_keys[x]].deleteChannel(room_ID)
        
        print(status)

    def rocketChatCreatePrivateGroup(self, platform_ID, subPlatform_ID, group_name):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())

        if (Main_Platform.getPlatformID == platform_ID):
            status, roomID = Main_Platform.createPrivateGroup(group_name)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, roomID = Subplatforms[sub_keys[x]].createPrivateGroup(group_name)
        
        print(status)
        print(roomID)

    def rocketChatDeletePrivateGroup(self, platform_ID, subPlatform_ID, room_ID):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())

        if (Main_Platform.getPlatformID == platform_ID):
            status = Main_Platform.deletePrivateGroup(room_ID)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status = Subplatforms[sub_keys[x]].deletePrivateGroup(room_ID)
        
        print(status)

    def rocketChatPostNewMessage(self, platform_ID, subPlatform_ID, room_ID, announcement):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())

        if (Main_Platform.getPlatformID == platform_ID):
            status, message = Main_Platform.postNewMessage(room_ID, announcement)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, message = Subplatforms[sub_keys[x]].postNewMessage(room_ID, announcement)
        
        print(status)
        print(message)

    def rocketChatCreateUserToken(self, platform_ID, subPlatform_ID, user_ID, username):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())

        if (Main_Platform.getPlatformID == platform_ID):
            status, token = Main_Platform.userToken(user_ID, username)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, token = Subplatforms[sub_keys[x]].userToken(user_ID, username)
        
        print(status)
        print(token)

    ##### Rocket Chat End #####
    
    def test(self):
        
        ###################### TEST: createPlatform ##############################
        print(self.createPlatform("Hackathon", {"TiddlyWiki"}))
        ##########################################################################

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
        # main_p = self.platformManager.createPlatform("TiddlyWiki", {})
        # print(self.startPlatform(main_p.getPlatformID(), {}))
        
        # print(self.stopPlatform(main_p.getPlatformID(), {}))
         
        #print(self.deletePlatform(main_p.getPlatformID(), {}))
        ##########################################################################
        
        
pi = PlatformInterface()
pi.test()