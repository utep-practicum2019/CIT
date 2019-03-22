from .ChappieEditor import PPTP_ConnectionsSublcass
from .IkesEditor import IKE_ConnectionsSublcass
from .Connections import Connections
#Input number of users to add
def addUsers(numberOfUsersInput):
    addedUsersArr=[]
    while True:
        # numberOfUsersInput = input("Enter number of users: ")
        # print(type(numberOfUsers))
        try:
            numberOfUsers = int(numberOfUsersInput)

            for x in range(numberOfUsers):
                #Call ChappieEditor.py and create user object
                currUserChappie=PPTP_ConnectionsSublcass()
                currUserChappie.createPassword()
                currUserChappie.pptpAddUser(currUserChappie.password)
                addedUsersArr.append(currUserChappie)
                # Call IkesEditor.py
                currUserIKE=IKE_ConnectionsSublcass()
                currUserIKE.password=currUserChappie.password
                currUserIKE.ikesAddUser(currUserIKE.password)
            # for x in range(numberOfUsers):
                # print(str(addedUsersArr[x].username) +" "+ 
                # str(addedUsersArr[x].password)+" " + str(addedUsersArr[x].pptpIP))
            return addedUsersArr
        except ValueError:
            # print("Must enter integer for number of users.")
            return False
def deleteUsers(users):
    for x in range(len(users)):
        emptyConn=Connections()
        # emptyConn.deleteUser(users[x],"ChappieTest.txt")
        emptyConn.deleteUser(users[x],"/etc/ppp/chap-secrets")
        # emptyConn.deleteUser(users[x],"IkesTest.txt")
        emptyConn.deleteUser(users[x],"/etc/ipsec.secrets")
    return True
def modifyUser(currUsername,newUsername,newPassword,newIP):
    emptyConn=Connections()
    emptyConn.modifyUser(currUsername,newUsername,newPassword,newIP)
    return True

# addUsers(10)
# users=["user2","user4","user6","user8","user10"]
# users=["Mario"]
# deleteUsers(users)
# modifyUser("Link","Mario","70099011","192.168.0.6")
# modifyUser("","Yoshi","70099011","192.168.0.6")