from random import randint
from Connections import Connections

class IKE_ConnectionsSublcass(Connections):
        def ikesAddUser(self,randomPassword):
                # ipsec=open("IkesTest.txt","a")
                ipsec=open("/etc/ipsec.secrets","a")
                # nextAvailableUser=super().checkCurUsers("IkesTest.txt")
                nextAvailableUser=super().checkCurUsers("/etc/ipsec.secrets")
                userNumVar=nextAvailableUser[0]
                # ipEND=nextAvailableUser[1]

                ipsec.write("user"+str(userNumVar)+ " %any%"+ " : "+ "EAP "+str(randomPassword)+"\n")
                userNumVar += 1
                ipsec.close()

# i=IKE_ConnectionsSublcass() 
# i.ikesInput(2)