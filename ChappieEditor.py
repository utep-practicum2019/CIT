from random import randint
from Connections import Connections

class PPTP_ConnectionsSublcass(Connections):
    def pptpAddUser(self, randomPassword,typeOfAdd):
        chapSec=open("ChappieTest.txt","a")
        # chapSec=open("/etc/ppp/chap-secrets","a")
        nextAvailableUser=super().checkCurUsers("ChappieTest.txt")
        # nextAvailableUser=super().checkCurUsers("/etc/ppp/chap-secrets")
        userNumVar=nextAvailableUser[0]
        ipEND=nextAvailableUser[1]
        if(typeOfAdd==True):
            distIP=" 192.168.0."
            chapSec.write("user"+str(userNumVar)+ " * "+str(randomPassword)+distIP+str(ipEND)+"\n")
            self.username="user"+str(userNumVar)
            self.pptpIP="192.168.0."+str(ipEND)
            chapSec.close()
        else:
            distIP=" 192.168.0."
            chapSec.write(self.username + " * "+str(randomPassword)+distIP+str(ipEND)+"\n")
            self.pptpIP="192.168.0."+str(ipEND)
            chapSec.close()
# p=PPTP_ConnectionsSublcass() 
# p.pptpAddUser(1)
# p.deleteUser("user2")