from random import randint
from .Connections import Connections

class L2TP_ConnectionsSublcass(Connections):
        def l2tpAddUser(self,randomPassword,typeOfAdd):
                # ipsec=open("L2TPTest.txt","a")
                ipsec=open("/etc/ipsec.secrets","a")
                # nextAvailableUser=super().checkCurUsers("L2TPTest.txt")
                nextAvailableUser=super().checkCurUsers("/etc/ipsec.secrets")
                userNumVar=nextAvailableUser[0]
                # ipEND=nextAvailableUser[1]
                if(typeOfAdd==True):
                        ipsec.write("SERVER_IP_ADDRESS " + " %any%"+ " : "+ "PSK "+str(randomPassword)+"\n")
                        userNumVar += 1
                        ipsec.close()
                else:
                        ipsec.write("SERVER_IP_ADDRESS " + " %any%"+ " : "+ "PSK "+str(randomPassword)+"\n")
                        userNumVar += 1
                        ipsec.close()

# i=IKE_ConnectionsSublcass() 
# i.ikesInput(2)