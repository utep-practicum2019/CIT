from random import randint
from Connections import Connections

class PPTP_ConnectionsSublcass(Connections):
    def pptpAddUser(self, randomPassword):
        # chapSec=open("ChappieTest.txt","a")
        chapSec=open("/etc/ppp/chap-secrets","a")
        # nextAvailableUser=super().checkCurUsers("ChappieTest.txt")
        nextAvailableUser=super().checkCurUsers("/etc/ppp/chap-secrets")
        userNumVar=nextAvailableUser[0]
        ipEND=nextAvailableUser[1]

        distIP=" 192.168.0."
        chapSec.write("user"+str(userNumVar)+ " * "+str(randomPassword)+distIP+str(ipEND)+"\n")
        self.username="user"+str(userNumVar)
        self.pptpIP="192.168.0."+str(ipEND)
        chapSec.close()
    def deleteUser(self, currUser):
        chapSec=open("ChappieTest.txt","r+")
        count=0
        for x in chapSec:
            if currUser in x:
                chapSec.write("what")
                # count+=1
                break
            # count+=1
        print(count)
        # chapSec=open("ChappieTest.txt","r+")
        # for x in chapSec
        #     if x==count:

        # chapSecNew=open("ChappieTestStorage.txt","r+")
        # #https://stackoverflow.com/questions/11968998/remove-lines-that-contain-certain-string
        # with chapSec as oldfile, chapSecNew as newfile:
        #     for line in oldfile:
        #         if currUser not in line:
        #             newfile.write(line)
        # chapSec=open("ChappieTest.txt","r+")
        # chapSecNew=open("ChappieTestStorage.txt","r+")
        # chapSec.truncate(0)
        # with chapSecNew as oldfile, chapSec as newfile:
        #     for line in oldfile:
        #         newfile.write(line)
        # chapSecNew=open("ChappieTestStorage.txt","r+")
        # chapSecNew.truncate(0)

# p=PPTP_ConnectionsSublcass() 
# p.pptpAddUser(1)
# p.deleteUser("user8")