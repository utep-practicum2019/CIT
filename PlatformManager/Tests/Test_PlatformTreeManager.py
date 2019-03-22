import unittest

import PlatformTreeManager

class Test_PlatformTreeManager(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.treeManager = PlatformTreeManager()
        
    def test_add(self):
        pass
    
    def test_remove(self):
        pass
    
    def test_getPlatform(self):
        pass
    
    def test_generate_main_ID(self):
        self.id = self.treeManager.generate_main_ID()
        self.assertTrue(1 <= self.id < 100000)
    
    def test_generate_sub_ID(self):
        pass