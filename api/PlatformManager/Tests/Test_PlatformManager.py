import unittest, sys, os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from PlatformsManager import PlatformsManager

class Test_Tiddlywiki(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        cls.platformManager = PlatformsManager()
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test_wiki_createPlatform(self):
        self.wiki = self.platformManager.createPlatform("TiddlyWiki", {})
        self.assertTrue(1 <= self.wiki[0] < 100000)
        
#     def test_wiki_addPlatform(self):
#         self.wiki = self.platformManager.createPlatform("TiddlyWiki", {})
#         self.wiki, self.rocketChat = self.platformManager.addPlatform(self.wiki[0], "RocketChat")
#         self.assertTrue(1 <= self.wiki[0] < 100000)
#         self.assertTrue(1 <= self.rocketChat['RocketChat'] < 100000) 
#         
    def test_wiki_createPlatform_with_subs(self):    
        self.wiki, self.hackathon = self.platformManager.createPlatform("TiddlyWiki", {"Hackathon"})
        self.assertTrue(1 <= self.wiki < 100000)
        self.assertTrue(1 <= self.hackathon["Hackathon"] < 100000)
#         
    def test_wiki_deletePlatform(self):
        self.wiki = self.platformManager.createPlatform("TiddlyWiki", {})
        self.id, self.status = self.platformManager.deletePlatform(self.wiki[0], {})
        self.assertTrue(1 <= self.id < 100000)
        self.assertEqual(self.status, "success")
        
#     def test_wiki_startPlatforms(self):
#         self.wiki, self.rocketChat = self.platformManager.createPlatform("TiddlyWiki", {"RocketChat"})
#         self.platformManager.startPlatforms(self.wiki, {self.rocketChat['RocketChat']})
#         #*****incomplete******
#         
#     def test_wiki_stopPlatforms(self):
#         self.wiki, self.rocketChat = self.platformManager.createPlatform("TiddlyWiki", {"RocketChat"})
#         self.platformManager.startPlatforms(self.wiki, {self.rocketChat['RocketChat']})
#         self.status = self.platformManager.stopPlatforms(self.wiki, {self.rocketChat['RocketChat']})
#         self.assertEqual(self.status, "Success")
#         
#     def test_wiki_requestForwarder(self):
#         pass
        
# class Test_RocketChat(unittest.TestCase):
#     
#     @classmethod
#     def setUpClass(cls):
#         cls.platformManager = PlatformsManager()
#     
#     @classmethod
#     def tearDownClass(cls):
#         pass
#     
#     def setUp(self):
#         pass
#     
#     def tearDown(self):
#         pass
#     
#     def test_rocketchat_createPlatform(self):
#         self.rocketchat = self.platformManager.createPlatform("RocketChat", {})
#         self.assertTrue(1 <= self.rocketchat < 100000)
#         
#     def test_rocketchat_addPlatform(self):
#         self.rocketchat = self.platformManager.createPlatform("RocketChat", {})
#         self.rocketchat, self.wiki = self.platformManager.addPlatform(self.rocketchat, "TiddlyWiki")
#         self.assertTrue(1 <= self.rocketchat < 100000)
#         self.assertTrue(1 <= self.wiki['TiddlyWiki'] < 100000) 
#         #####check return type of addPlatform#####
#         
#     def test_rocketchat_createPlatform_with_subs(self):   
#         self.rocketchat, self.wiki = self.platformManager.createPlatform("RocketChat", {"TiddlyWiki"})
#         self.assertTrue(1 <= self.rocketchat < 100000)
#         self.assertTrue(1 <= self.wiki['TiddlyWiki'] < 100000)
#         #####check return type of addPlatform##### 
#         
#     def test_rocketchat_deletePlatform(self):
#         self.rocketchat = self.platformManager.createPlatform("RocketChat", {})
#         self.id, self.status = self.platformManager.deletePlatform(self.rocketchat, {})
#         self.assertTrue(1 <= self.id < 100000)
#         self.assertEqual(self.status, "success")
#         
#     def test_rocketchat_startPlatforms(self):
#         self.rocketchat, self.wiki = self.platformManager.createPlatform("RocketChat", {"TiddlyWiki"})
#         self.platformManager.startPlatforms(self.rocketchat, {self.wiki['TiddlyWiki']})
#         #*****incomplete******
#         
#     def test_rocketchat_stopPlatforms(self):
#         self.rocketchat, self.wiki = self.platformManager.createPlatform("RocketChat", {"TiddlyWiki"})
#         self.platformManager.startPlatforms(self.rocketchat, {self.wiki['TiddlyWiki']})
#         self.status = self.platformManager.stopPlatforms(self.rocketchat, {self.wiki['TiddlyWiki']})
#         self.assertEqual(self.status, "Success")
#         
#     def test_rocketchat_requestForwarder(self):
#         pass
#     
class Test_Hackathon(unittest.TestCase):
     
    @classmethod
    def setUpClass(cls):
        cls.platformManager = PlatformsManager()
#     
#     @classmethod
#     def tearDownClass(cls):
#         pass
#      
#     def setUp(self):
#         pass
#         
#     def tearDown(self):
#         pass
#         
    def test_hackathon_createPlatform(self):
        self.hackathon = self.platformManager.createPlatform("Hackathon", {})
        self.assertTrue(1 <= self.hackathon[0] < 100000)
#         
#     def test_hackathon_addPlatform(self):
#         self.hackathon = self.platformManager.createPlatform("Hackathon", {})
#         self.hackathon, self.wiki = self.platformManager.addPlatform(self.hackathon, "TiddlyWiki")
#         self.assertTrue(1 <= self.hackathon < 100000)
#         self.assertTrue(1 <= self.wiki['TiddlyWiki'] < 100000) 
#         #####check return type of addPlatform#####
#         
    def test_hackathon_createPlatform_with_subs(self):    
        self.hackathon, self.wiki = self.platformManager.createPlatform("Hackathon", {"TiddlyWiki"})
        self.assertTrue(1 <= self.hackathon < 100000)
        self.assertTrue(1 <= self.wiki['TiddlyWiki'] < 100000)
#         
    def test_hackathon_deletePlatform(self):
        self.hackathon = self.platformManager.createPlatform("Hackathon", {})
        self.id, self.status = self.platformManager.deletePlatform(self.hackathon[0], {})
        self.assertTrue(1 <= self.id < 100000)
        self.assertEqual(self.status, "success")
#         
#     def test_hackathon_startPlatforms(self):
#         self.hackathon, self.wiki = self.platformManager.createPlatform("Hackathon", {"TiddlyWiki"})
#         self.platformManager.startPlatforms(self.hackathon, {self.wiki['TiddlyWiki']})
#         #*****incomplete******
#         
#     def test_hackathon_stopPlatforms(self):
#         self.hackathon, self.wiki = self.platformManager.createPlatform("Hackathon", {"TiddlyWiki"})
#         self.platformManager.startPlatforms(self.hackathon, {self.wiki['TiddlyWiki']})
#         self.status = self.platformManager.stopPlatforms(self.hackathon, {self.wiki['TiddlyWiki']})
#         self.assertEqual(self.status, "Success")
#         
#     def test_hackathon_requestForwarder(self):
#         pass
                
if __name__ == '__main__':
    unittest.main()