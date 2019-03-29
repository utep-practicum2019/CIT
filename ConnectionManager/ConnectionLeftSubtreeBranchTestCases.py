from ChappieEditor import PPTP_ConnectionsSublcass
from IkesEditor import IKE_ConnectionsSublcass
from Connections import Connections
import Configure
#Configure.py test cases
print("Configure.py test cases")
#Adds users to ChappieTest.txt and IkesTest.txt
configureCorrectArr=[]
configureCorrectArr=Configure.addUsers(2)
print("Correct returned user values when attempting to add 2 users")
for x in range(2):
     print(configureCorrectArr[x].username +" "+ configureCorrectArr[x].password+" " + configureCorrectArr[x].pptpIP)
print("Receive error message when sending in a non-integer value R")
configureBadARR=Configure.addUsers("R")

print("\n")

#Connections.py test cases
print("Connections.py test cases")
#Create connections object
testUser=Connections()
print("Initial Connections object user info: ")
print(testUser.username +" "+testUser.password+" "+testUser.pptpIP)
#Create new password for object
testUser.createPassword()
print("Password after calling createPassword: "+testUser.password)
#Check what current user number and current IP address end would be
print("Test checkCurUsers function for next available user in current test files.")
testNextAvailUserChap=Connections().checkCurUsers("ChappieTest.txt")
print("Next available ChappieTest.txt user number: " +str(testNextAvailUserChap[0]))
print("Next available ChappieTest.txt IP end: "+str(testNextAvailUserChap[1]))
testNextAvailUserIke=Connections().checkCurUsers("IkesTest.txt")
print("Next available IkesTest.txt user number: " +str(testNextAvailUserIke[0])+"\n")

#ChappieEditor.py test cases
print("ChappieEditor.py test cases")
chappieTestConObj=PPTP_ConnectionsSublcass()
chappieTestConObj.password="22222222"
chappieTestConObj.pptpAddUser(chappieTestConObj.password)
print("Created user and password from test run of pptpAddUser:")
print("User: "+chappieTestConObj.username+" IP: "+chappieTestConObj.pptpIP+"\n")

#IkesEditor.py test cases
print("IkesEditor.py test cases")
ikesTestConObj=IKE_ConnectionsSublcass()
ikesTestConObj.password="33333333"
ikesTestConObj.ikesAddUser(ikesTestConObj.password)
print("Created user and password from test run of ikesAddUser:")
print("User: "+chappieTestConObj.username+" IP: "+chappieTestConObj.pptpIP+"\n")