import time

import requests

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
        self.cit_url = 'http://0.0.0.0:5001'
        self.database_path = '/api/v2/resources/database'
        self.database_url = self.cit_url + self.database_path

    ##### Platform Manager #####

    def createPlatform(self, main_platform, subplatforms):
        Main_Platform = self.platformManager.createPlatform(main_platform, subplatforms)
        status = "Failure"

        if (Main_Platform != "Failure"):
            if ((Main_Platform.get_sub_platforms() == {}) and (subplatforms != [])):
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

                self.formatCreateUpdateRequest(Main_Platform, 0)

                return response
            else:
                return {"Status": status, "Response": {}}
        else:
            return {"Status": status, "Response": {}}

    def deletePlatform(self, platform_ID, subplatform_IDs):
        Main_Platform = self.platformManager.deletePlatform(platform_ID, subplatform_IDs)
        deletions = []

        if (Main_Platform != False or Main_Platform[0] != None):
            status = Main_Platform[1]
            if (subplatform_IDs == []):
                deletions.append(platform_ID)
                self.formatDeleteRequest(platform_ID, deletions)
            else:
                for x in subplatform_IDs:
                    deletions.append(x)
                    self.formatDeleteRequest(platform_ID, deletions)
        else:
            status = "Failure"

        return status

    def addPlatform(self, platform_ID, subplatforms):
        Main_Platform = self.platformManager.addPlatform(platform_ID, subplatforms)
        status = "Failure"

        if (Main_Platform != "Failure"):
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

                self.formatCreateUpdateRequest(Main_Platform, 1)

                return response
            else:
                return {"Status": status, "Response": {}}
        else:
            return {"Status": status, "Response": {}}

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
                    time.sleep(5)
                    if (self.platformManager.check_service(Subplatforms[x]) == False):
                        status = "Failure"
                        break

            if (status != "Failure"):
                response = self.createResponse(Main_Platform[0], status, 1)

                return response
            else:
                return {"Status": status, "Response": {}}
        else:
            return {"Status": status, "Response": {}}

    def stopPlatform(self, platform_ID, subplatform_IDs):
        Main_Platform = self.platformManager.stopPlatforms(platform_ID, subplatform_IDs)
        status = "Failure"

        if (Main_Platform != "Failure"):
            Subplatforms = Main_Platform[0].get_sub_platforms()

            if (Main_Platform[1] == "Success"):
                status = "Success"
                time.sleep(5)

            if (self.platformManager.check_service(Main_Platform[0]) == False):
                for x in Subplatforms:
                    if (self.platformManager.check_service(Subplatforms[x]) == True):
                        status = "Failure"
                        break

            if (status != "Failure"):
                response = self.createResponse(Main_Platform[0], status, 1)

                return response
            else:
                return {"Status": status, "Response": {}}
        else:
            return {"Status": status, "Response": {}}

    def getPlatformStatus(self, main_ID, subplatform_ID=0):
        Main_Platform = self.platformManager.getPlatform(main_ID)
        if (subplatform_ID == 0):
            status = self.platformManager.check_service(Main_Platform)
        else:
            Subplatforms = Main_Platform.get_sub_platforms()
            for x in Subplatforms:
                if (Subplatforms[x].getPlatformID() == subplatform_ID):
                    status = self.platformManager.check_service(Subplatforms[x])
                    break

        return status

    def requestHandler(self, main_ID, subplatform_ID, command):
        Main_Platform = self.platformManager.getPlatform(main_ID)

        if (Main_Platform is None):
            return {"success": False}

        if (subplatform_ID == 0):
            return Main_Platform.requestHandler(command)
        else:
            subplatform = None
            subplatforms = Main_Platform.get_sub_platforms()

            for x in subplatforms:
                if (subplatform_ID == subplatforms[x].getPlatformID()):
                    subplatform = subplatforms[x]
                    break

            if (subplatform is None):
                print("Subplatform not found")
                return {"success": False}
            else:
                return subplatform.requestHandler(command)

    def editPlatformAlias(self, main_ID, alias, subplatform_ID=0):
        Main_Platform = self.platformManager.getPlatform(main_ID)

        if (Main_Platform is None):
            return {"success": False}

        if (subplatform_ID == 0):
            Main_Platform.setPlatformAlias(alias)
            self.formatCreateUpdateRequest(Main_Platform, 1)
            return {"success": True}
        else:
            subplatform = None
            subplatforms = Main_Platform.get_sub_platforms()

            for x in subplatforms:
                if (subplatform_ID == subplatforms[x].getPlatformID()):
                    subplatform = subplatforms[x]
                    break

            if (subplatform is None):
                print("Subplatform not found")
                return {"success": False}
            else:
                subplatform.setPlatformAlias(alias)
                self.formatCreateUpdateRequest(Main_Platform, 1)
                return {"success": True}

    def editPlatformNote(self, main_ID, note, subplatform_ID=0):
        Main_Platform = self.platformManager.getPlatform(main_ID)

        if (Main_Platform is None):
            return {"success": False}

        if (subplatform_ID == 0):
            Main_Platform.setPlatformNote(note)
            self.formatCreateUpdateRequest(Main_Platform, 1)
            return {"success": True}
        else:
            subplatform = None
            subplatforms = Main_Platform.get_sub_platforms()

            for x in subplatforms:
                if (subplatform_ID == subplatforms[x].getPlatformID()):
                    subplatform = subplatforms[x]
                    break

            if (subplatform is None):
                print("Subplatform not found")
                return {"success": False}
            else:
                subplatform.setPlatformNote(note)
                self.formatCreateUpdateRequest(Main_Platform, 1)
                return {"success": True}

    ##### End Platform Manager #####

    ##### Utility #####

    def createResponse(self, Main_Platform, status, type):
        platform = Main_Platform
        Subplatforms = platform.get_sub_platforms()

        if (type == 0):
            response0 = {"Status": status,
                         "Response": {"Main_Platform": {platform.getPlatformName(): platform.getPlatformID()},
                                      "Subplatforms": {}}
                         }
        else:
            response1 = {"Status": status,
                         "Response": {platform.getPlatformName(): [platform.getPlatformID(), platform.getIpPort()]}
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

    def formatCreateUpdateRequest(self, Main_Platform, type):
        Subplatforms = Main_Platform.get_sub_platforms()

        platform_data = {"main": {"id": Main_Platform.getPlatformID(),
                                  "ip_port": Main_Platform.getIpPort(),
                                  "name": Main_Platform.getPlatformName(),
                                  "alias": Main_Platform.getPlatformAlias(),
                                  "note": Main_Platform.getPlatformNote(),
                                  "date_created": Main_Platform.getPlatformDateCreated()},
                         "subplatforms": []
                         }

        for x in Subplatforms:
            platform_data["subplatforms"].append({"id": Subplatforms[x].getPlatformID(),
                                                  "ip_port": Subplatforms[x].getIpPort(),
                                                  "name": Subplatforms[x].getPlatformName(),
                                                  "alias": Subplatforms[x].getPlatformAlias(),
                                                  "note": Subplatforms[x].getPlatformNote(),
                                                  "date_created": Subplatforms[x].getPlatformDateCreated()
                                                  })

        request_data = {"collection_name": "platforms",
                        "document_id": platform_data["main"]["id"],
                        "document": platform_data
                        }

        if (type == 0):
            r = requests.post(self.database_url, json=request_data)
        elif (type == 1):
            r = requests.put(self.database_url, json=request_data)

        if (r.status_code == requests.codes.ok):
            return True

        return False

    def formatDeleteRequest(self, main_ID, deletions):
        if (len(deletions) == 0):
            request_data = {
                "collection_name": "platforms",
                "document_id": main_ID
            }
            r = requests.delete(self.database_url, json=request_data)

            if r.status_code == requests.codes.ok:
                return True
            return False
        else:
            for to_delete in deletions:
                request_data = {
                    "collection_name": "platforms",
                    "document_id": to_delete
                }
                r = requests.delete(self.database_url, json=request_data)

                if r.status_code != requests.codes.ok:
                    return False
            return True

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

    def deletePlugin(self, plugin_name):
        self.pluginManager.deletePlatform(plugin_name)
        return True

    def getAvailablePlugins(self):
        available_plugins = self.pluginManager.getAvailablePlugins()
        return available_plugins

    ##### End Plugin Manager #####

    ##### Rocket Chat #####

    def rocketChatRegisterUser(self, platform_ID, subplatform_ID, user_email, username, user_pass, user_nick):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        userID = ''

        if (Main_Platform.getPlatformName() == "Rocketchat"):
            status, userID = Main_Platform.registerUser(user_email, username, user_pass)
        else:
            for x in range(0, len(sub_keys)):
                if (Subplatforms[sub_keys[x]].getPlatformName() == "Rocketchat"):
                    status, userID = Subplatforms[sub_keys[x]].registerUser(user_email, username, user_pass)

        return {"Status": status, "User_ID": userID}

    def rocketChatLoginUser(self, platform_ID, subPlatform_ID, username, user_pass):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        authToken = ''

        if (Main_Platform.getPlatformName() == "Rocketchat"):
            status, authToken = Main_Platform.loginUser(username, user_pass)
        else:
            for x in range(0, len(sub_keys)):
                if (Subplatforms[sub_keys[x]].getPlatformName() == "Rocketchat"):
                    status, authToken = Subplatforms[sub_keys[x]].loginUser(username, user_pass)

        return {"Status": status, "Auth_Token": authToken}

    def rocketChatGetUserInfo(self, platform_ID, subPlatform_ID, user_ID, username):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        userID = ''
        email = ''
        userName = ''
        userNick = ''

        if (Main_Platform.getPlatformName() == "Rocketchat"):
            status, userID, email, userName, userNick = Main_Platform.getUserInfo(user_ID, username)
        else:
            for x in range(0, len(sub_keys)):
                if (Subplatforms[sub_keys[x]].getPlatformName() == "Rocketchat"):
                    status, userID, email, userName, userNick = Subplatforms[sub_keys[x]].getUserInfo(user_ID, username)

        return {"Status": status, "User_ID": userID, "Email": email, "Username": userName, "Nickname": userNick}

    def rocketChatDeleteUser(self, platform_ID, subPlatform_ID, user_ID):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = "Failure"
        result = False

        if (Main_Platform.getPlatformName() == "Rocketchat"):
            result = Main_Platform.deleteUser(user_ID)
        else:
            for x in range(0, len(sub_keys)):
                if (Subplatforms[sub_keys[x]].getPlatformName() == "Rocketchat"):
                    result = Subplatforms[sub_keys[x]].deleteUser(user_ID)

        if (result == True):
            status = "Success"

        return status

    def rocketChatCreateChannel(self, platform_ID, subPlatform_ID, channel_name):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        channelID = ''

        if (Main_Platform.getPlatformName() == "Rocketchat"):
            status, channelID = Main_Platform.createChannel(channel_name)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformName() == "Rocketchat"):
                    status, channelID = Subplatforms[sub_keys[x]].createChannel(channel_name)

        return {"Status": status, "Channel_ID": channelID}

    def rocketChatDeleteChannel(self, platform_ID, subPlatform_ID, channel_ID):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = "Failure"
        result = False

        if (Main_Platform.getPlatformName() == "Rocketchat"):
            result = Main_Platform.deleteChannel(channel_ID)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformName() == "Rocketchat"):
                    result = Subplatforms[sub_keys[x]].deleteChannel(channel_ID)

        if (result == True):
            status = "Success"

        return status

    def rocketChatCreatePrivateGroup(self, platform_ID, subPlatform_ID, group_name):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        roomID = ''

        if (Main_Platform.getPlatformName() == "Rocketchat"):
            status, roomID = Main_Platform.createPrivateGroup(group_name)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformName() == "Rocketchat"):
                    status, roomID = Subplatforms[sub_keys[x]].createPrivateGroup(group_name)

        return {"Status": status, "Room_ID": roomID}

    def rocketChatDeletePrivateGroup(self, platform_ID, subPlatform_ID, room_ID):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = "Failure"
        result = False

        if (Main_Platform.getPlatformName() == "Rocketchat"):
            result = Main_Platform.deletePrivateGroup(room_ID)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformName() == "Rocketchat"):
                    result = Subplatforms[sub_keys[x]].deletePrivateGroup(room_ID)

        if (result == True):
            status = "Success"

        return status

    def rocketChatPostNewMessage(self, platform_ID, subPlatform_ID, room_ID, announcement):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        message = ''

        if (Main_Platform.getPlatformName() == "Rocketchat"):
            status, message = Main_Platform.postNewMessage(room_ID, announcement)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformName() == "Rocketchat"):
                    status, message = Subplatforms[sub_keys[x]].postNewMessage(room_ID, announcement)

        return {"Status": status, "Message": message}

    def addUserGroup(self, platform_ID, roomID, userID):
        Main_Platform = self.platformManager.getPlatform(platform_ID)
        Subplatforms = Main_Platform.get_sub_platforms()
        sub_keys = list(Subplatforms.keys())
        status = ''
        room_ID = ''

        if (Main_Platform.getPlatformName() == "Rocketchat"):
            status, room_ID = Main_Platform.addUserGroup(roomID, userID)
        else:
            for x in range(0, len(sub_keys)):
                print(Subplatforms[sub_keys[x]].getPlatformID())

                if (Subplatforms[sub_keys[x]].getPlatformName() == "Rocketchat"):
                    status, room_ID = Subplatforms[sub_keys[x]].postNewMessage(roomID, userID)

        return {"Status": status, "Room_ID": room_ID}

    ##### End Rocket Chat #####
