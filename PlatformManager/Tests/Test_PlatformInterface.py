import unittest
import re

from PlatformManager.PlatformInterface import PlatformInterface

class Test_PlatformInterface(unittest.TestCase):
    
    platform_interface = PlatformInterface()
    
    def test_forward_request(self):
        response = self.platform_interface.forward_request("generic.json")
        expected = str({'destination': 'user1', 'response': 'http-server /home/practicum/Documents/tiddlywikis/genericWiki/output -a 0.0.0.0 -p 8085'})
        
        response = re.sub('["]', '', response)
        expected = re.sub('[\']', '', expected)
        
        print(response)
        print(expected)
        
        self.assertEqual(expected, response)
        
#Test_PlatformInterface.test_forward_request(Test_PlatformInterface)