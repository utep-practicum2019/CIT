import unittest, sys, os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from .Platforms.Hackathon import Hackathon

class Test_Hackathon(unittest.TestCase):
    platform = Hackathon()

    def test_getLink(self):
        link = self.platform.getLink()
        self.assertEqual(link, " ") 
    
    def test_getIpPort(self):
        ipPort = self.platform.getIpPort()
        self.assertEqual(ipPort, " ")
        
    def test_getPlatformName(self):
        name = self.platform.getPlatformName()
        self.assertEqual(name, " ")
        
    def test_getPlatformInstallation(self):
        install = self.platform.getPlatformInstallation()
        self.assertEqual(install, " ")
        
    def test_getPlatformVersion(self):
        link = self.platform.getPlatformVersion()
        self.assertEquals(link, " ")
        
    def test_getPlatformID(self):
        id = self.platform.getPlatformID()
        self.assertEquals(id, 0)
        
    def test_get_start_command(self):
        command = self.platform.get_start_command()
        self.assertEquals(command, " ")

    def test_get_stop_command(self):
        command = self.platform.get_stop_command()
        self.assertEquals(command, " ")
        
    def test_get_sub_platforms(self):
        subPlatforms = self.platform.get_sub_platforms()
        self.assertEquals(subPlatforms, { })
        
if __name__ == '__main__':
    unittest.main()