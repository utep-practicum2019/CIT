import unittest, re, json, sys, os, time

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from PlatformInterface import PlatformInterface

class Test_PlatformInterface(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.platformInterface = PlatformInterface()

    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_createPlatform(self):
        response = self.platformInterface.createPlatform("Hackathon", {"TiddlyWiki"})
        
        print("\nTest: Create Platform")
        print("Response: "+str(response))    
        print("Status: "+response["Status"]+"\n")
        
        self.assertEqual(response["Status"], "Success")
        #self.assertDictEqual(response[1], {'Main_Platform': {'Hackathon': 11410}, 'Subplatforms': {'TiddlyWiki': 92553}})
        pass

    def test_deletePlatform(self):
        platform = self.platformInterface.createPlatform("Rocketchat", {"TiddlyWiki"})
        response = self.platformInterface.deletePlatform(platform["Response"]["Main_Platform"]["Rocketchat"], {})
        
        print("\nTest: Delete Platform")
        print("Response: "+str(response))    
        print("Status: "+response+"\n")
        
        self.assertEqual(response, "Success")
        pass

    def test_addPlatform(self):
        platform = self.platformInterface.createPlatform("Hackathon", {})
        response = self.platformInterface.addPlatform(platform["Response"]["Main_Platform"]["Hackathon"], {"Rocketchat"})
        
        print("\nTest: Add Platform")
        print("Before Addition: "+str(platform["Response"]))
        print("Response: "+str(response))    
        print("Status: "+response["Status"]+"\n")
        
        self.assertEqual(response["Status"], "Success")
        pass

    def test_startStopPlatform(self):
    #     platform = self.platformInterface.createPlatform("Rocketchat", {"TiddlyWiki"})
    #     start_response = self.platformInterface.startPlatform(platform[1]["Main_Platform"]["Rocketchat"], platform[1]["Subplatforms"]["TiddlyWiki"])
        
    #     print("\nTest: Start Platform")
    #     print("Response: "+str(start_response))    
    #     print("Status: "+start_response["Status"]+"\n")
        
    #     self.assertEqual(start_response["Status"], "Success")
        
    #     stop_response = self.platformInterface.stopPlatform(platform[1]["Main_Platform"]["Rocketchat"], platform[1]["Subplatforms"]["TiddlyWiki"])

    #     print("\nTest: Stop Platform")
    #     print("Response: "+str(stop_response))    
    #     print("Status: "+stop_response["Status"]+"\n")

    #     self.assertEqual(stop_response["Status"], "Success")
        pass

    # def test_getPlatform(self):
    #     pass

    # def test_addPlugin(self):
    #     pass

    # def test_deletePlugin(self):
    #     pass

    # def test_getAvailablePlugins(self):
    #     # response = self.platformInterface.getAvailablePlugins()
    #     # print(response)
    #     pass

    # def test_loadPlatform(self):
    #     pass

class Test_PlatformInterfaceRocketChat(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.platformInterface = PlatformInterface()
    #     cls.platform = cls.platformInterface.createPlatform("Rocketchat", {})
    #     time.sleep(5)
    #     cls.platformInterface.startPlatform(cls.platform[1]["Main_Platform"]["Rocketchat"], {})
    #     time.sleep(10)
        
    #     cls.user = "test1"
    #     cls.user_mail = cls.user+"@mail.com"
    #     cls.password = "q1w2e3"
    #     cls.channel_name = "channel100"
    #     cls.room_name = "room100"

    #     cls.status, cls.userID = cls.platformInterface.rocketChatRegisterUser(cls.platform[1]["Main_Platform"]["Rocketchat"], 0, cls.user_mail, cls.user, cls.password, cls.user)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.platformInterface.stopPlatform(cls.platform[1]["Main_Platform"]["Rocketchat"], {})
    
    def test_RocketChatRegisterUser(self):
        # response = self.platformInterface.rocketChatRegisterUser(self.platform[1]["Main_Platform"]["Rocketchat"], 0, "test2@mail.com", "test2", "a1s2d3", "test2")
        # time.sleep(5)
        # self.assertTrue(response[0])
        # self.platformInterface.rocketChatDeleteUser(self.platform[1]["Main_Platform"]["Rocketchat"], 0, response[1])
        pass

    def test_RocketChatLoginUser(self):
        # response = self.platformInterface.rocketChatLoginUser(self.platform[1]["Main_Platform"]["Rocketchat"], 0, self.user, self.password)
        # self.assertTrue(response[0])
        pass

    def test_RocketChatGetUserInfo(self):
        # response = self.platformInterface.rocketChatGetUserInfo(self.platform[1]["Main_Platform"]["Rocketchat"], 0, self.userID, self.user)
        # self.assertTrue(response[0])
        pass

    def test_RocketChatDeleteUser(self):
        # response = self.platformInterface.rocketChatDeleteUser(self.platform[1]["Main_Platform"]["Rocketchat"], 0, self.userID)
        # self.assertTrue(response)
        pass

    def test_RocketChatCreateChannel(self):
        # response = self.platformInterface.rocketChatCreateChannel(self.platform[1]["Main_Platform"]["Rocketchat"], 0, self.channel_name)
        # self.assertTrue(response[0])
        pass

    def test_RocketChatDeleteChannel(self):
        # status, channelID = self.platformInterface.rocketChatCreateChannel(self.platform[1]["Main_Platform"]["Rocketchat"], 0, "channel200")
        # time.sleep(5)
        # response = self.platformInterface.rocketChatDeleteChannel(self.platform[1]["Main_Platform"]["Rocketchat"], 0, channelID)
        # self.assertTrue(response)
        pass

    def test_RocketChatCreatePrivateGroup(self):
        # response = self.platformInterface.rocketChatCreatePrivateGroup(self.platform[1]["Main_Platform"]["Rocketchat"], 0, self.room_name)
        # self.assertTrue(response[0])
        pass

    def test_RocketChatDeletePrivateGroup(self):
        # status, roomID = self.platformInterface.rocketChatCreatePrivateGroup(self.platform[1]["Main_Platform"]["Rocketchat"], 0, "room200")
        # time.sleep(5)
        # response = self.platformInterface.rocketChatDeletePrivateGroup(self.platform[1]["Main_Platform"]["Rocketchat"], 0, roomID)
        # time.sleep(5)
        # self.assertTrue(response)
        pass

    def test_RocketChatPostNewMessage(self):
        # status, roomID = self.platformInterface.rocketChatCreatePrivateGroup(self.platform[1]["Main_Platform"]["Rocketchat"], 0, "room300")
        # time.sleep(5)
        # response = self.platformInterface.rocketChatPostNewMessage(self.platform[1]["Main_Platform"]["Rocketchat"], 0, "room300", "TEST MESSAGE")
        # time.sleep(5)
        # self.platformInterface.rocketChatDeletePrivateGroup(self.platform[1]["Main_Platform"]["Rocketchat"], 0, roomID)
        # self.assertTrue(response[0])
        pass



















    
    # @staticmethod
    # def generate_JSON(platform, request, requester):
    #     with open("JSON_Test_Files/test.json", "r+") as json_file:
    #         data = json.load(json_file)
            
    #         data["platform"] = platform
    #         data["request"] = request
    #         data["requester"] = requester
            
    #         json_file.seek(0)
    #         json.dump(data, json_file)
    #         json_file.truncate()
            
    # def test_get(self):
    #     Test_PlatformInterface.generate_JSON("wiki", "start", "user1")
    #     response = re.sub('["]', '', self.platformInterface.get("JSON_Test_Files/test.json"))
    #     expected = re.sub('[\']', '', str({'destination': 'user1', 'response': 'http-server /home/practicum/Documents/tiddlywikis/genericWiki/output -a 0.0.0.0 -p 8085'}))
        
    #     print("Test: Wiki Start")
    #     print("Response: "+response)
    #     print("Expected: "+expected+"\n")
        
    #     self.assertEqual(expected, response)
        
    #     Test_PlatformInterface.generate_JSON("wiki", "stop", "user1")
    #     response = re.sub('["]', '', self.platformInterface.get("JSON_Test_Files/test.json"))
    #     expected = re.sub('[\']', '', str({'destination': 'user1', 'response': 'kill 1201'}))
        
    #     print("Test: Wiki Stop")
    #     print("Response: "+response)
    #     print("Expected: "+expected+"\n")
        
    #     self.assertEqual(expected, response)
        
    #     Test_PlatformInterface.generate_JSON("chat", "start", "user1")
    #     response = re.sub('["]', '', self.platformInterface.get("JSON_Test_Files/test.json"))
    #     expected = re.sub('[\']', '', str({'destination': 'user1', 'response': 'service snap.rocketchat-server.rocketchat-server start'}))
        
    #     print("Test: Chat Start")
    #     print("Response: "+response)
    #     print("Expected: "+expected+"\n")
        
    #     self.assertEqual(expected, response)
        
    #     Test_PlatformInterface.generate_JSON("chat", "stop", "user1")
    #     response = re.sub('["]', '', self.platformInterface.get("JSON_Test_Files/test.json"))
    #     expected = re.sub('[\']', '', str({'destination': 'user1', 'response': 'service snap.rocketchat-server.rocketchat-server stop'}))
        
    #     print("Test: Chat Stop")
    #     print("Response: "+response)
    #     print("Expected: "+expected+"\n")
        
#     self.assertEqual(expected, response)