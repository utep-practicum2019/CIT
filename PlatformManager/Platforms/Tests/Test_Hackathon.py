import unittest 
from .Platforms.Hackathon import Hackathon

class Test_Hackathon():

    def testGetLink():
        platform = None

    def __init__():
        self.platform = Hackathon()

    def test_getLink(self):
        link = platform.getLink()
        assertEquals(link, "tiddly.com")
       
    def test_getIpPort(self):
        ipPort = platform.getIpPort()
        assertEquals(ipPort, "0.0.0.0:8085")
        
    def test_getPlatformName(self):
        name = platform.getPlatformName()
        assertEquals(name, "tiddly wiki")
        
    def test_getPlatformInstallation(self):
        install = platform.getPlatformInstallation()
        assertEquals(install, "/installation")
        
    def test_getPlatformVersion(self):
        link = platform.getPlatformVersion()
        assertEquals(link, "5.1.20-prerelease")
        
    def test_getPlatformID(self):
        id = platform.getPlatformID()
        assertEquals(link, 0)
        
    def test_get_start_command(self):
        command = platform.get_start_command()
        assertEquals(command, "http-server /home/practicum/Documents/tiddlywikis/genericWiki/output -a 0.0.0.0 -p 8085")

    def test_get_stop_command(self):
        command = platform.get_stop_command()
        assertEquals(command, "kill 1200")
        
    def test_get_sub_platforms(self):
        subPlatforms = platform.get_sub_platforms()
        assertEquals(subPlatforms, {"chat", "wiki"})
        
if __name__ == '__main__':
    unittest.main()