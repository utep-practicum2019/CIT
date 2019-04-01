import time, json, requests

from .PlatformsManager import PlatformsManager
from .PluginManager import PluginManager

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platform interface. 
            The platform interface provides callable functions within the platform manager subsystem.
"""
class PlatformInterface():
    
    def __init__(self):
        self.platformManager = PlatformsManager()
        self.pluginManager = PluginManager()
        self.cit_url = 'http://127.0.0.1:5000'
        self.database_path = '/api/v2/resources/database'
        self.database_url = self.cit_url + self.database_path
          
    ##### Platform Manager #####
    
    def createPlatform(self, main_platform, subplatforms): 
        Main_Platform = self.platformManager.createPlatform(main_platform, subplatforms)
        status = "Failure"

        if (Main_Platform != False):
            if ((Main_Platform.get_sub_platforms() == { }) and (subplatforms != { })):
                print("Error in subplatform creation")
            else:    
                Subplatforms = Main_Platform.get_sub_platforms()
                sub_keys = list(Subplatforms.keys())
        
            if ((1 <= Main_Platform.getPlatformID() < 100000) and (len(sub_keys) != 0)):
                for x in range(0, len(sub_keys)):
                    if (1 <= Subplatforms[sub_keys[x]].getPlatformID() < 100000):
                        status = "Success"
                    else:
                        status = "Failure"
                        break
            elif (1 <= Main_Platform.getPlatformID() < 100000):
                status = "Success"
                    
            if (status != "Failure"):
                response = self.createResponse(Main_Platform, status, 0)

                request_result = self.formatCreateRequest(Main_Platform)

                return response
            else:
                return {"Status" : status, "Response" : {}}
        else:
            return {"Status" : status, "Response" : {}}

    def deletePlatform(self, platform_ID, subplatform_IDs):
        Main_Platform = self.platformManager.deletePlatform(platform_ID, subplatform_IDs)
        deletions = []

        if (Main_Platform != False):
            status = Main_Platform[1]

            if (subplatform_IDs == { }):
                deletions.append(platform_ID)
                request_result = self.formatDeleteRequest(platform_ID, deletions)
            else:
                for x in subplatform_IDs:
                    deletions.append(x)
                    request_result = self.formatDeleteRequest(platform_ID, deletions)
        else:
            status = "Failure"

        return status

    def addPlatform(self, platform_ID, subplatforms):
        before_add = self.getIDs(platform_ID)
        Main_Platform = self.platformManager.addPlatform(platform_ID, subplatforms)
        status = "Failure"

        if (Main_Platform != False):
            after_add = self.getIDs(platform_ID)
            additions = list(set(before_add) - set(after_add))
            Subplatforms = Main_Platform.get_sub_platforms()
            sub_keys = list(Subplatforms.keys())

            if (1 <= Main_Platform.getPlatformID() < 100000):
                for x in range(0, len(sub_keys)):
                    if (1 <= Subplatforms[sub_keys[x]].getPlatformID() < 100000):
                        status = "Success"
                    else:
                        status = "Failure"
                        break
            
            if (status != "Failure"):
                response = self.createResponse(Main_Platform, status, 0)

                request_result = self.formatUpdateRequest(platform_ID, additions)
                    
                return response
            else:
                return {"Status" : status, "Response" : {}}
        else:
            return {"Status" : status, "Response" : {}}
    
    def startPlatform(self, platform_ID, subplatform_IDs): 
        Main_Platform = self.platformManager.startPlatforms(platform_ID, subplatform_IDs)
        status = "Failure"
        
        if (Main_Platform != "Failure"):
            Subplatforms = Main_Platform[0].get_sub_platforms()
            
            if (Main_Platform[1] == "Success"):
                status = "Success"
                time.sleep(5)

            if (self.platformManager.check_service(Main_Platform[0]) == True):
                for x in Subplatforms:
                    if(self.platformManager.check_service(Subplatforms[x]) == False):
                        status = "Failure"
                        break
            
            if (status != "Failure"):
                response = self.createResponse(Main_Platform, status, 1)

                return response
            else:
                return {"Status" : status, "Response" : {}}
        else:
            return {"Status" : status, "Response" : {}}

    def stopPlatform(self, platform_ID, subplatform_IDs): 
        Main_Platform = self.platformManager.stopPlatforms(platform_ID, subplatform_IDs)
        status = "Failure"

        if (Main_Platform != "Failure"):
            Subplatforms = Main_Platform[0].get_sub_platforms()
        
            if (Main_Platform[1] == "Success"):
                status = "Success"
                time.sleep(5)

            if (self.platformManager.check_service(Main_Platform) == False):
                for x in Subplatforms:
                    if(self.platformManager.check_service(Subplatforms[x]) == True):
                        status = "Failure"
                        break

            if (status != "Failure"):
                response = self.createResponse(Main_Platform, status, 1)

                return response
            else:
                return {"Status" : status, "Response" : {}}
        else:
            return {"Status" : status, "Response" : {}}

    # def getPlatform(self, platform_ID, subplatform_IDs): 
    #     Main_Platform = self.platformManager.getPlatform(platform_ID)
    #     Subplatforms = Main_Platform[0].get_sub_platforms()
    #     response = {}
    #     info = []
    #     info.append({"name" : Main_Platform.getPlatformName(),
    #                 "ip:port" : Main_Platform.getIPPort()})

    #     if (subplatform_IDs != { }):
    #         for x in Subplatforms:
    #             info.append({"name" : subplatform_IDs[x].getPlatformName(),
    #                         "ip:port" : subplatform_IDs[x].getIpPort()})

    #     response = {info}
                    
    #     return response
    
    ##### End Platform Manager #####

    ##### Utility #####

    def createResponse(self, Main_Platform, status, type):
        platform = Main_Platform
        Subplatforms = platform.get_sub_platforms()

        if (type == 0):
            response0 = {"Status" : status, 
                        "Response" : {"Main_Platform": {platform.getPlatformName() : platform.getPlatformID()}, "Subplatforms": {}}
                        }
        else:
            response1 = {"Status" : status, 
                        "Response" : {platform.getPlatformName() : {platform.getPlatformID(), platform.getIpPort}}
                        }
    
        for x in Subplatforms:
            name = Subplatforms[x].getPlatformName()

            if (type == 0):
                response0["Response"]["Subplatforms"][name] = Subplatforms[x].getPlatformID()
            else:
                response1["Response"][name] = {Subplatforms[x].getPlatformID(), Subplatforms[x].getIpPort()}
        
        if (type == 0):
            return response0
        else:
            return response1

    def formatCreateRequest(self, main_platform):
        Subplatforms = main_platform.get_sub_platforms()

        platform_data = {"main" : {"id" : main_platform.getPlatformID(),
                        "ip_port" : main_platform.getIpPort(),
                        "name" : main_platform.getPlatformName()},
                        "subplatforms": []
                        }
        
        for x in Subplatforms:
            platform_data["subplatforms"].append({"id" : Subplatforms[x].getPlatformID(),
                                                "ip_port" : Subplatforms[x].getIpPort(),
                                                "name" : Subplatforms[x].getPlatformName()
                                                }) 
        
        r = requests.post(self.database_url, json=platform_data)
    
        if r.status_code == requests.codes.ok:
            return True

        return False

    def formatDeleteRequest(self, main_ID, deletions):
        deleted_platform_data = {"main" : main_ID,
                                "deletions" : deletions}
        
        r = requests.delete(self.database_url, json=deleted_platform_data)
    
        if r.status_code == requests.codes.ok:
            return True

        return False

    def formatUpdateRequest(self, main_ID, additions):
        added_platform_data = {"main" : main_ID,
                                "additions" : []}
        
        for x in additions:
            platform = self.platformManager.getPlatform(x)
            
            added_platform_data["additions"].append({"id" : platform.getPlatformID(),
                                                    "ip_port" : platform.getIpPort(),
                                                    "name" : platform.getPlatformName()
                                                    })
        
        r = requests.put(self.database_url, json=added_platform_data)
    
        if r.status_code == requests.codes.ok:
            return True

        return False

    def getIDs(self, main_platform_ID):
        ids = []
        Main_Platform = self.platformManager.getPlatform(main_platform_ID)
        Subs = Main_Platform.get_sub_platforms()

        ids.append(Main_Platform.getPlatformID())
        for x in Subs:
            ids.append(Subs[x].getPlatformID())
        
        return ids

    ##### End Utility #####

    ##### Plugin Manager #####
    
    def addPlugin(self, path): 
        pass
    
    def deletePlugin(self, plugin_Name): 
        pass
    
    def getAvailablePlugins(self): 
        available_plugins = self.pluginManager.getAvailablePlugins()

        return {"Plugins" : available_plugins}

    def loadPlatform(self):
        pass

    ##### End Plugin Manager #####

    ##### Rocket Chat #####

    def rocketChatRegisterUser(self, platform_ID, subplatform_ID, user_email, username, user_pass, user_nick):
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

        return {status, userID}
                
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

        return {status, authToken}
    
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

        return {status, userID, email, userName, userNick}
    
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
        
        return {status, channelID} 

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
        
        return {status, roomID} 

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

        return {status, message}

    # def rocketChatCreateUserToken(self, platform_ID, subPlatform_ID, user_ID, username):
    #     Main_Platform = self.platformManager.getPlatform(platform_ID)
    #     Subplatforms = Main_Platform.get_sub_platforms()
    #     sub_keys = list(Subplatforms.keys())
    #     status = ''
    #     token = ''

    #     if (Main_Platform.getPlatformID == platform_ID):
    #         status, token = Main_Platform.userToken(user_ID, username)
    #     else:
    #         for x in range(0, len(sub_keys)):
    #             print(Subplatforms[sub_keys[x]].getPlatformID())

    #             if (Subplatforms[sub_keys[x]].getPlatformID() == subPlatform_ID):
    #                 status, token = Subplatforms[sub_keys[x]].userToken(user_ID, username)
        
    #     print(status)
    #     print(token)

    #     return (status, token) 

    ##### End Rocket Chat #####
    
    def test(self):
        pass
        ###################### TEST: createPlatform ##############################
        # print(self.createPlatform("Hackathon", {"TiddlyWiki"}))
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
        
        # print(self.deletePlatform(main_p.getPlatformID(), {}))
        ##########################################################################
        
        ################### TEST: startPlatform/stopPlatform #####################
        # main_p = self.platformManager.createPlatform("TiddlyWiki", {})
        # print(self.startPlatform(main_p.getPlatformID(), {}))
        
        # print(self.stopPlatform(main_p.getPlatformID(), {}))
         
        #print(self.deletePlatform(main_p.getPlatformID(), {}))
        ##########################################################################

        ##################### TEST: registerUser/loginUser #######################
        # main_p = self.platformManager.createPlatform("Rocketchat", {})
        
        # print(self.startPlatform(main_p.getPlatformID(), {}))
        # time.sleep(10)
        # print(self.rocketChatRegisterUser(main_p.getPlatformID(), 0, "bozosrevenge2@mail.com", "BozosRevenge2", "Q1W2E5", "BozosRevenge2"))
        # time.sleep(10)
        # print(self.rocketChatLoginUser(main_p.getPlatformID(), 0, "BozosRevenge2", "Q1W2E5"))
        # time.sleep(10)
        # print(self.stopPlatform(main_p.getPlatformID(), {}))
        ##########################################################################

        ############## TEST: registerUser/getUserInfo/deleteUser #################
        
        # main_p = self.platformManager.createPlatform("Rocketchat", {"TiddlyWiki"})
        # print(self.startPlatform(main_p.getPlatformID(), {}))
        # time.sleep(10)
        
        # status, USERID = self.rocketChatRegisterUser(main_p.getPlatformID(), 0, "bb1@mail.com", "bb1", "Q1W2E5", "bb1")
        # time.sleep(60)
        # print(self.rocketChatGetUserInfo(main_p.getPlatformID(), 0, USERID, "bb1"))
        # time.sleep(60)
        # print(self.rocketChatDeleteUser(main_p.getPlatformID(), 0, USERID))
        # time.sleep(10)
        # print(self.stopPlatform(main_p.getPlatformID(), {}))
        
        ##########################################################################

        ### TEST: createChannel/createPrivateGroup/deleteChannel/deletePrivateGroup ###
        # main_p = self.platformManager.createPlatform("Rocketchat", {})
        # print(self.startPlatform(main_p.getPlatformID(), {}))
        # time.sleep(20)
        # status, channel_ID = self.rocketChatCreateChannel(main_p.getPlatformID(), 0, "bozoreturns1")
        # time.sleep(5)
        # status, room_ID = self.rocketChatCreatePrivateGroup(main_p.getPlatformID(), 0, "TeamBozo")
        # time.sleep(30)
        # print(self.rocketChatDeleteChannel(main_p.getPlatformID(), 0, channel_ID))
        # time.sleep(10)
        # print(self.rocketChatDeletePrivateGroup(main_p.getPlatformID(), 0, room_ID))
        # time.sleep(120)
        # print(self.stopPlatform(main_p.getPlatformID(), {}))
        
        ##############################################################################
        
pi = PlatformInterface()
pi.test()