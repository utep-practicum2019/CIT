import unittest, sys, os 

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from PlatformManager.Platforms.tmp.Submission import Submission

class Test_Submission(unittest.TestCase):
    platform = Submission()

    def test_getLink(self):
        link = self.platform.getLink()
        self.assertEqual(link, "tiddly.com") 
    
    def test_getIpPort(self):
        ipPort = self.platform.getIpPort()
        self.assertEqual(ipPort, "0.0.0.0:8085")
        
    def test_getPlatformName(self):
        name = self.platform.getPlatformName()
        self.assertEqual(name, "tiddly wiki")
        
    def test_getPlatformInstallation(self):
        install = self.platform.getPlatformInstallation()
        self.assertEqual(install, "/installation")
        
    def test_getPlatformVersion(self):
        link = self.platform.getPlatformVersion()
        self.assertEquals(link, "5.1.20-prerelease")
        
    def test_getPlatformID(self):
        id = self.platform.getPlatformID()
        self.assertEquals(id, 10)
        
    def test_get_start_command(self):
        command = self.platform.get_start_command()
        self.assertEquals(command, "http-server /home/practicum/Documents/tiddlywikis/genericWiki/output -a 0.0.0.0 -p 8085")

    def test_get_stop_command(self):
        command = self.platform.get_stop_command()
        self.assertEquals(command, "kill 1201")
        
    def test_get_sub_platforms(self):
        subPlatforms = self.platform.get_sub_platforms()
        self.assertEquals(subPlatforms, {"chat", "wiki"})
        
if __name__ == '__main__':
    unittest.main()