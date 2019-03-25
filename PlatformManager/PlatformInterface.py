import json, time
from PlatformsManager import PlatformsManager
from PluginManager import PluginManager

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom interface. 
            The platform interface provides callable functions within the platform manager subsystem.
"""

class PlatformInterface():
    #cit_IP = "http://127.0.0.1:"
    
    def __init__(self):
        self.platformManager = PlatformsManager()
        self.pluginManager = PluginManager()
        
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
    
    def createPlatform(self, main_platform, subplatforms): 
        Main_Platform = self.platformManager.createPlatform(main_platform, subplatforms)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        response = self.createResponse(Main_Platform)
        
        status = "Failure"
        
        if (1 <= Main_Platform.getPlatformID() < 100000):
            for x in range(0, len(sub_keys)):
                if (1 <= Subplatforms[sub_keys[x]].getPlatformID() < 100000):
                    status = "Success"
                    
        return (status, response)

    def deletePlatform(self, platform_ID, subplatform_IDs): 
        Main_Platform = self.platformManager.deletePlatform(platform_ID, subplatform_IDs)
        #response = self.createResponse(Main_Platform[0])
            
        status = Main_Platform[1]
                        
        return status

    def addPlatform(self, platform_ID, subplatforms): 
        Main_Platform = self.platformManager.addPlatform(platform_ID, subplatforms)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        response = self.createResponse(Main_Platform)
        
        status = "Failure"
        
        if (1 <= Main_Platform.getPlatformID() < 100000):
            for x in range(0, len(sub_keys)):
                if (1 <= Subplatforms[sub_keys[x]].getPlatformID() < 100000):
                    status = "Success"
                    
        return (status, response)
    
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

    ##### Utility #####

    def createResponse(self, Main_Platform):
        dictionary = {"Main_Platform": {}, "Subplatforms": {}}
        platform = Main_Platform
        dictionary["Main_Platform"] = {platform.getPlatformName() : platform.getPlatformID()}
        subplatforms = platform.get_sub_platforms()
    
        for x in subplatforms:
            name = subplatforms[x].getPlatformName()
            dictionary["Subplatforms"][name] = subplatforms[x].getPlatformID()
        
        return dictionary

    def startStopResponse(self, Main_Platform):
        dictionary = {"Main_Platform": {}, "Subplatforms": {}}
        platform = Main_Platform
        dictionary["Main_Platform"] = {platform.getPlatformName() : platform.getPlatformID()}
        subplatforms = platform.get_sub_platforms()
    
        for x in subplatforms:
            name = subplatforms[x].getPlatformName()
            dictionary["Subplatforms"][name] = subplatforms[x].getPlatformID()
        
        return dictionary

    ##### End Utility #####
    
    ##### Plugin Manager #####
    
    def addPlugin(self, path): 
        pass
    
    def deletePlugin(self, plugin_Name): 
        pass
    
    def getAvailablePlugins(self): 
        available_plugins = self.pluginManager.getAvailablePlugins()

        return {available_plugins}
    
    def loadPlatform(self):
        pass
    
    ##### End Plugin Manager #####

    ##### Rocket Chat #####
    
    def rocketChatRegisterUser(self, platform_ID, subplatform_ID, user_email, username, user_pass, usernick):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        userID = ''

        if (Main_Platform.getPlatformID() == platform_ID):
            status, userID = Main_Platform.registerUser(user_email, username, user_pass)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subplatform_ID):
                    status, userID = Subplatforms[sub_keys[x]].registerUser(user_email, username, user_pass, user_nick)

        print(status)
        print(userID)
        
        return(status, userID)
                
    def rocketChatLoginUser(self, platform_ID, subPlatform_ID, username, user_pass):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        authToken = ''

        if (Main_Platform.getPlatformID() == platform_ID):
            status, authToken = Main_Platform.loginUser(username, user_pass)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, authToken = Subplatforms[sub_keys[x]].loginUser(username, user_pass)

        print(status)
        print(authToken)

        return (status, authToken)
    
    def rocketChatGetUserInfo(self, platform_ID, subPlatform_ID, user_ID, username): 
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        userID = ''
        email = ''
        userName = ''
        userNick = ''
        
        if (Main_Platform.getPlatformID() == platform_ID):
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

        return(status, userID, email, userName, userNick)
    
    def rocketChatDeleteUser(self, platform_ID, subPlatform_ID, user_ID):
        print(user_ID)
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''

        if (Main_Platform.getPlatformID() == platform_ID):
            status = Main_Platform.deleteUser(user_ID)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status = Subplatforms[sub_keys[x]].deleteUser(user_ID)
        print(status)

        return status

    def rocketChatCreateChannel(self, platform_ID, subPlatform_ID, channel_name):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        channelID = ''

        if (Main_Platform.getPlatformID() == platform_ID):
            status, channelID = Main_Platform.createChannel(channel_name)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, channelID = Subplatforms[sub_keys[x]].createChannel(channel_name)
        
        print(status)
        print(channelID)

        return (status, channelID) 

    def rocketChatDeleteChannel(self, platform_ID, subPlatform_ID, channel_ID):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''

        if (Main_Platform.getPlatformID() == platform_ID):
            status = Main_Platform.deleteChannel(channel_ID)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status = Subplatforms[sub_keys[x]].deleteChannel(channel_ID)
        
        print(status)

        return status 

    def rocketChatCreatePrivateGroup(self, platform_ID, subPlatform_ID, group_name):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        roomID = ''

        if (Main_Platform.getPlatformID() == platform_ID):
            status, roomID = Main_Platform.createPrivateGroup(group_name)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, roomID = Subplatforms[sub_keys[x]].createPrivateGroup(group_name)
        
        print(status)
        print(roomID)
        
        return (status, roomID) 

    def rocketChatDeletePrivateGroup(self, platform_ID, subPlatform_ID, room_ID):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''

        if (Main_Platform.getPlatformID() == platform_ID):
            status = Main_Platform.deletePrivateGroup(room_ID)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status = Subplatforms[sub_keys[x]].deletePrivateGroup(room_ID)
        
        print(status)
        
        return status

    def rocketChatPostNewMessage(self, platform_ID, subPlatform_ID, room_ID, announcement):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        message = ''

        if (Main_Platform.getPlatformID() == platform_ID):
            status, message = Main_Platform.postNewMessage(room_ID, announcement)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, message = Subplatforms[sub_keys[x]].postNewMessage(room_ID, announcement)
        
        print(status)
        print(message)

        return (status, message)

    def rocketChatCreateUserToken(self, platform_ID, subPlatform_ID, user_ID, username):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        token = ''

        if (Main_Platform.getPlatformID() == platform_ID):
            status, token = Main_Platform.userToken(user_ID, username)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
                    status, token = Subplatforms[sub_keys[x]].userToken(user_ID, username)
        
        print(status)
        print(token)

        return (status, token) 

    ##### End Rocket Chat #####
    
    def test(self):
        pass
        ###################### TEST: createPlatform ##############################
        #print(self.createPlatform("Hackathon", {"TiddlyWiki"}))
        ##########################################################################

        ###################### TEST: deletePlatform ##############################
        # main_p = self.platformManager.createPlatform("Hackathon", {"TiddlyWiki"})
        # # #print(main_p)
         
        # print("Deleting: ")
        # #subplatforms = main_p.get_sub_platforms()
        # print(self.deletePlatform(main_p.getPlatformID(),{}))
        ##########################################################################
        
        #################### TEST: deletePlatform(no subs) #######################
        # main_p = self.platformManager.createPlatform("Hackathon", {})
        # print(main_p)
           
        # print(self.deletePlatform(main_p.getPlatformID(), {}))
        ##########################################################################
        
        ########################## TEST: addPlatform #############################
        # main_p = self.platformManager.createPlatform("Hackathon", {})
        # print(self.addPlatform(main_p.getPlatformID(), {"TiddlyWiki"}))
        
        #print(self.deletePlatform(main_p.getPlatformID(), {}))
        ##########################################################################
        
        ################### TEST: startPlatform/stopPlatform #####################
        # main_p = self.platformManager.createPlatform("TiddlyWiki", {})
        # print(self.startPlatform(main_p.getPlatformID(), {}))
        
        # print(self.stopPlatform(main_p.getPlatformID(), {}))
         
        #print(self.deletePlatform(main_p.getPlatformID(), {}))
        ##########################################################################

        ##################### TEST: registerUser/loginUser #######################

        '''0
        main_p = self.platformManager.createPlatform("Rocketchat", {})
        
        print(self.startPlatform(main_p.getPlatformID(), {}))
        time.sleep(10)
        print(self.rocketChatRegisterUser(main_p.getPlatformID(), 0, "bozosrevenge2@mail.com", "BozosRevenge2", "Q1W2E5", "BozosRevenge2"))
        time.sleep(10)
        print(self.rocketChatLoginUser(main_p.getPlatformID(), 0, "BozosRevenge2", "Q1W2E5"))
        time.sleep(10)
        print(self.stopPlatform(main_p.getPlatformID(), {}))
        '''
        ##########################################################################

        ############## TEST: registerUser/getUserInfo/deleteUser #################
        '''
        main_p = self.platformManager.createPlatform("Rocketchat", {})
        print(self.startPlatform(main_p.getPlatformID(), {}))
        time.sleep(10)
        
        status, USERID = self.rocketChatRegisterUser(main_p.getPlatformID(), 0, "bb@mail.com", "bb", "Q1W2E5", "bb")
        time.sleep(10)
        print(self.rocketChatGetUserInfo(main_p.getPlatformID(), 0, USERID, "bb"))
        time.sleep(30)
        print(self.rocketChatDeleteUser(main_p.getPlatformID(), 0, USERID))
        #time.sleep(10)
        #print(self.stopPlatform(main_p.getPlatformID(), {}))
        '''
        ##########################################################################

        ### TEST: createChannel/createPrivateGroup/deleteChannel/deletePrivateGroup ###
        main_p = self.platformManager.createPlatform("Rocketchat", {})
        print(self.startPlatform(main_p.getPlatformID(), {}))
        time.sleep(5)
        status, channel_ID = self.rocketChatCreateChannel(main_p.getPlatformID(), 0, "bozoreturns1")
        time.sleep(5)
        status, room_ID = self.rocketChatCreatePrivateGroup(main_p.getPlatformID(), 0, "TeamBozo")
        time.sleep(30)
        print(self.rocketChatDeleteChannel(main_p.getPlatformID(), 0, channel_ID))
        time.sleep(10)
        print(self.rocketChatDeletePrivateGroup(main_p.getPlatformID(), 0, room_ID))
        time.sleep(10)
        print(self.stopPlatform(main_p.getPlatformID(), {}))
        ##############################################################################
        
pi = PlatformInterface()
pi.test()