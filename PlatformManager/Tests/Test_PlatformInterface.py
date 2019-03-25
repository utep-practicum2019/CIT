import unittest
import re
import json

from PlatformInterface import PlatformInterface

class Test_PlatformInterface(unittest.TestCase):
    
    platform_interface = PlatformInterface()
    
    @staticmethod
    def generate_JSON(platform, request, requester):
        with open("JSON_Test_Files/test.json", "r+") as json_file:
            data = json.load(json_file)
            
            data["platform"] = platform
            data["request"] = request
            data["requester"] = requester
            
            json_file.seek(0)
            json.dump(data, json_file)
            json_file.truncate()
            
    def test_get(self):
        Test_PlatformInterface.generate_JSON("wiki", "start", "user1")
        response = re.sub('["]', '', self.platform_interface.get("JSON_Test_Files/test.json"))
        expected = re.sub('[\']', '', str({'destination': 'user1', 'response': 'http-server /home/practicum/Documents/tiddlywikis/genericWiki/output -a 0.0.0.0 -p 8085'}))
        
        print("Test: Wiki Start")
        print("Response: "+response)
        print("Expected: "+expected+"\n")
        
        self.assertEqual(expected, response)
        
        Test_PlatformInterface.generate_JSON("wiki", "stop", "user1")
        response = re.sub('["]', '', self.platform_interface.get("JSON_Test_Files/test.json"))
        expected = re.sub('[\']', '', str({'destination': 'user1', 'response': 'kill 1201'}))
        
        print("Test: Wiki Stop")
        print("Response: "+response)
        print("Expected: "+expected+"\n")
        
        self.assertEqual(expected, response)
        
        Test_PlatformInterface.generate_JSON("chat", "start", "user1")
        response = re.sub('["]', '', self.platform_interface.get("JSON_Test_Files/test.json"))
        expected = re.sub('[\']', '', str({'destination': 'user1', 'response': 'service snap.rocketchat-server.rocketchat-server start'}))
        
        print("Test: Chat Start")
        print("Response: "+response)
        print("Expected: "+expected+"\n")
        
        self.assertEqual(expected, response)
        
        Test_PlatformInterface.generate_JSON("chat", "stop", "user1")
        response = re.sub('["]', '', self.platform_interface.get("JSON_Test_Files/test.json"))
        expected = re.sub('[\']', '', str({'destination': 'user1', 'response': 'service snap.rocketchat-server.rocketchat-server stop'}))
        
        print("Test: Chat Stop")
        print("Response: "+response)
        print("Expected: "+expected+"\n")
        
        self.assertEqual(expected, response)