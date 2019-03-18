import unittest, sys, os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from ..PlatformsManager import PlatformsManager

class Test_Tiddlywiki(unittest.TestCase):
    

    def test_configurePlatforms(self):
        platformManager = PlatformsManager()
        wiki = platformManager.configurePlatform("CREATE", "TiddlyWiki", {"Rocket Chat"})

        
if __name__ == '__main__':
    unittest.main()