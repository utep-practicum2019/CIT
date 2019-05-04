import unittest
from .ChappieEditor import PPTP_ConnectionsSublcass
from .IkesEditor import IKE_ConnectionsSublcass
from .Connections import Connections
import Configure

#For all test cases need to uncomment test files in all four classes and comment out filepaths 

class UserConnectionsTestDriver(unittest.TestCase):
    #Configure.py test cases
    #Adds users to ChappieTest.txt and IkesTest.txt
    def test_1_Configure_AddUsers_ChapAndIke(self):
        configureCorrectArr=[]
        configureCorrectArr=Configure.addUsers(1)
        self.assertEqual(type(configureCorrectArr[0]), PPTP_ConnectionsSublcass)
        configureBadARR=[]
        configureBadARR=Configure.addUsers("R")
        self.assertFalse(configureBadARR)
    #tests deleteUsers with set parameters
    def test_2_Configure_DeleteUsers_ChapandIke(self):
        #write fake users to be delated to ChappieTest.txt
        chapSec=open("ChappieTest.txt","a")
        chapSec.write("Mario"+ " * "+"11111111"+" "+"1.1.1.1"+"\n")
        chapSec.write("Yoshi"+ " * "+"22222222"+" "+"2.2.2.2"+"\n")
        chapSec.close()
        #write fake users to be delted to IkesTest.txt
        ipsec=open("IkesTest.txt","a")
        ipsec.write("Mario"+ " %any%"+ " : "+ "EAP "+"11111111"+"\n")
        ipsec.write("Yoshi"+ " %any%"+ " : "+ "EAP "+"22222222"+"\n")
        ipsec.close()
        #delete Mario check for return of true
        users=["Mario"]
        deleteTestResult=Configure.deleteUsers(users)
        self.assertEqual(deleteTestResult,True)
    #tests modifyUser on previously entered user Yoshi to change to Bowser
    def test_3_Configure_ModifyUser_ChapandIke(self):
        modifyTestResult=Configure.modifyUser("Yoshi","Bowser","33333333","3.3.3.3")
        self.assertEqual(modifyTestResult,True)
    def test_4_Configure_FileAddUsers_ChapandIke(self):
        testUsers=["Mario","Yoshi","Luigi","Peach","Toad"]
        testUsersArr=[]
        testUsersArr=Configure.fileAddUsers(testUsers)
        self.assertEqual(type(testUsersArr[0]),PPTP_ConnectionsSublcass)

    #Connections.py test cases
    #tests general user functionality for user objects, checking current user, and creating a password
    def test_5_Connections_GeneralUserFunctionality(self): 
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
    #tests deleteUsers with set parameters
    def test_6_Connections_DeleteUsers(self):
        chapBool=False
        ipSecBool=False
        testUser=Connections()
        #write fake users to be delated to ChappieTest.txt
        chapSec=open("ChappieTest.txt","a")
        chapSec.write("Link"+ " * "+"11111111"+" "+"1.1.1.1"+"\n")
        chapSec.write("Zelda"+ " * "+"22222222"+" "+"2.2.2.2"+"\n")
        chapSec.close()
        #write fake users to be delted to IkesTest.txt
        ipsec=open("IkesTest.txt","a")
        ipsec.write("Link"+ " %any%"+ " : "+ "EAP "+"11111111"+"\n")
        ipsec.write("Zelda"+ " %any%"+ " : "+ "EAP "+"22222222"+"\n")
        ipsec.close()
        #deletes user Zelda from both files. Verifies by boolean
        testUser.deleteUser("Zelda","ChappieTest.txt")
        testUser.deleteUser("Zelda","IkesTest.txt")
        #Checks if Zelda is not in either file after delete
        chapSec=open("ChappieTest.txt","r")
        ipsec=open("IkesTest.txt","r")
        if 'Zelda' not in chapSec.read():
            chapBool=True
        if 'Zelda' not in ipsec.read():
            ipSecBool=True
        chapSec.close()
        ipsec.close()
        self.assertEqual(chapBool,True)
        self.assertEqual(ipSecBool,True)
        #tests modifyUser on previously entered user Link to change to Ganon
    def test_7_Configure_ModifyUser(self):
        testUser=Connections()
        chapBool=False
        ipSecBool=False
        testUser.modifyUser("Link","Ganon","33333333","3.3.3.3")
        # Checks if Link is not in either file after modify and Ganon is
        chapSec=open("ChappieTest.txt","r")
        ipsec=open("IkesTest.txt","r")
        if 'Ganon' in chapSec.read():
            chapBool=True
        if 'Ganon' in ipsec.read(): 
            ipSecBool=True
        chapSec.close()
        ipsec.close()
        self.assertEqual(chapBool,True)
        self.assertEqual(ipSecBool,True)

    # ChappieEditor.py test cases
    def test_8_ChappieEditorAddUser(self):
        chappieTestConObj=PPTP_ConnectionsSublcass()
        chappieTestConObj.password="22222222"
        chappieTestConObj.pptpAddUser(chappieTestConObj.password,True)
        #Check created user is formated correctly
        self.assertIn("user",chappieTestConObj.username)
        self.assertIn("192.168.0.",chappieTestConObj.pptpIP) 

    #IkesEditor.py test cases
    def test_9_IkesEditorAddUser(self):
        ikesTestConObj=IKE_ConnectionsSublcass()
        ikesTestConObj.password="33333333"
        ikesTestConObj.ikesAddUser(ikesTestConObj.password,True)
        #Check created user is formated correctly
        self.assertIn("user",ikesTestConObj.username)

if __name__ == '__main__':
    unittest.main()