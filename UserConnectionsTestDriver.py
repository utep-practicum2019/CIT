import unittest
from ChappieEditor import PPTP_ConnectionsSublcass
from IkesEditor import IKE_ConnectionsSublcass
from Connections import Connections
import Configure
class UserConnectionsTestDriver(unittest.TestCase):
     #Configure.py test cases
     #Adds users to ChappieTest.txt and IkesTest.txt
    def test_Configure_AddUsers_ChapAndIke(self):
          configureCorrectArr=[]
          configureCorrectArr=Configure.addUsers(1)
          self.assertEqual(type(configureCorrectArr[0]), PPTP_ConnectionsSublcass)
          configureBadARR=[]
          configureBadARR=Configure.addUsers("R")
          self.assertFalse(configureBadARR)
    #Connections.py test cases
    def test_Connections(self): 
        #Create connections object
        testUser=Connections()
        #checks username was creted correctly
        self.assertIn("user",testUser.username)
        #checks password was created correctly by checking it's an integer
        self.assertEqual(type(int(testUser.password)),int)   
        #checks IP is correctly assigned
        self.assertIn("192.168.0.",testUser.pptpIP)     
        #Create new password for object and check that the new password is an int and 8 digits
        testUser.createPassword()
        self.assertEqual(type(int(testUser.password)),int)
        self.assertEqual(len(str(testUser.password)),8)
        #Check what current user number and current IP address end would be and if it's greater than 0
        testNextAvailUserChap=Connections().checkCurUsers("ChappieTest.txt")
        self.assertGreater(testNextAvailUserChap[0],0)
        self.assertGreater(testNextAvailUserChap[1],0)
        #Check what current user number is available for IKE and that it is greater than 1
        testNextAvailUserIke=Connections().checkCurUsers("IkesTest.txt")
        self.assertGreater(testNextAvailUserIke[0],0)
    #ChappieEditor.py test cases
    def test_ChappieEditor(self):
        chappieTestConObj=PPTP_ConnectionsSublcass()
        chappieTestConObj.password="22222222"
        chappieTestConObj.pptpAddUser(chappieTestConObj.password)
        #Check created user is formated correctly
        self.assertIn("user",chappieTestConObj.username)
        self.assertIn("192.168.0.",chappieTestConObj.pptpIP) 
    #IkesEditor.py test cases
    def test_IkesEditor(self):
        ikesTestConObj=IKE_ConnectionsSublcass()
        ikesTestConObj.password="33333333"
        ikesTestConObj.ikesAddUser(ikesTestConObj.password)
        #Check created user is formated correctly
        self.assertIn("user",ikesTestConObj.username)

if __name__ == '__main__':
    unittest.main()