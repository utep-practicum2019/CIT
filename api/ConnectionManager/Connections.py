from random import randint

class Connections():
    username="userx"
    password="11111111"
    pptpIP="192.168.0.0"

    def addUsers(self):
        pass

    def createPassword(self):
        passwordLength=0
        while(passwordLength!=8):
            randomPassword=randint(00000000,99999999)
            passwordLength=len(str(randomPassword))
        self.password=str(randomPassword)

    def checkCurUsers(self,secretsFile):
        userNumVar=0
        ipEND=0
        currUserCounter=1
        currIP_END_Counter=2
        baseIP="192.168.0."
        baseUser="user"
        chapSecrets=open(secretsFile,"r+") 
        with chapSecrets as read:
            for currLine in read:
                # if(currLine[0][0]!='#' and currLine[0][0] != '1' and currLine[0][0] != '\n'):
                currUser=baseUser+str(currUserCounter)+"_"
                # print(currUser)
                # currIP=baseIP+str(currIP_END_Counter)
                # if currUser in currLine or currIP in currLine:
                # if currUser not in open(secretsFile).read() and currIP not in open(secretsFile).read():
                #     userNumVar=currUserCounter
                #     ipEND=currIP_END_Counter
                #     print("if "+str(userNumVar)+str(ipEND))
                #     break
                chapSecrets1=open(secretsFile,"r+") 
                if currUser not in chapSecrets1.read():
                    userNumVar=currUserCounter
                    chapSecrets.close()
                    chapSecrets1.close()
                    # print("1elif "+str(userNumVar))
                    break
                # elif currIP not in open(secretsFile).read():
                #     # userNumVar=currUserCounter
                #     ipEND=currIP_END_Counter
                #     print("2elif "+str(userNumVar)+str(ipEND))
                #     break
                chapSecrets1.close()
                currUserCounter+=1
                # currIP_END_Counter+=1
        chapSecrets=open(secretsFile,"r+") 
        with chapSecrets as read:
            for currLine in read:
                # if(currLine[0][0]!='#' and currLine[0][0] != '1' and currLine[0][0] != '\n'):
                # currUser=baseUser+str(currUserCounter)
                currIP=baseIP+str(currIP_END_Counter)
                # print (currIP)
                # if currUser in currLine or currIP in currLine:
                # if currUser not in open(secretsFile).read() and currIP not in open(secretsFile).read():
                #     userNumVar=currUserCounter
                #     ipEND=currIP_END_Counter
                #     print("if "+str(userNumVar)+str(ipEND))
                #     break
                # elif currUser not in open(secretsFile).read():
                #     userNumVar=currUserCounter
                #     ipEND=currIP_END_Counter+1
                #     print("1elif "+str(userNumVar)+str(ipEND))
                #     break
                chapSecrets1=open(secretsFile,"r+")
                if currIP not in chapSecrets1.read():
                    # userNumVar=currUserCounter
                    ipEND=currIP_END_Counter
                    chapSecrets.close()
                    chapSecrets1.close()
                    # print("2elif "+str(ipEND))
                    break
                # currUserCounter+=1
                chapSecrets1.close()
                currIP_END_Counter+=1
        if userNumVar == 0:
            userNumVar=currUserCounter  
            # print("end user if "+str(userNumVar))
        if ipEND == 0:
            ipEND=currIP_END_Counter
            # print("end ip if "+str(ipEND))
        # print(userNumVar)
        # print(ipEND)
        return [userNumVar, ipEND]

    def deleteUser(self, currUser,fileName):
        tempFile="configTempFile.txt"
        configFile=open(fileName,"r+") 
        configTempFile=open(tempFile,"r+")
        #https://stackoverflow.com/questions/11968998/remove-lines-that-contain-certain-string
        with configFile as oldfile, configTempFile as newfile:
            for line in oldfile:
                if currUser not in line:
                    newfile.write(line)
        configFile.close()
        configTempFile.close()
        configFile=open(fileName,"r+")
        configTempFile=open(tempFile,"r+")
        configFile.truncate(0)
        with configTempFile as oldfile, configFile as newfile:
            for line in oldfile:
                newfile.write(line)
        configTempFile=open(tempFile,"r+")
        configTempFile.truncate(0)
        configFile.close()
        configTempFile.close()

    def modifyUser(self, currUsername,newUsername,newPassword,newIP):
        # chapFile="ChappieTest.txt"
        chapFile="/etc/ppp/chap-secrets"
        # ikeFile="IkesTest.txt"
        ikeFile="/etc/ipsec.secrets"
        self.deleteUser(currUsername,chapFile)
        self.deleteUser(currUsername,ikeFile)

        # chapSec=open("ChappieTest.txt","a")
        chapSec=open("/etc/ppp/chap-secrets","a")
        chapSec.write(newUsername+ " * "+newPassword+" "+newIP+"\n")
        chapSec.close()

        # ipsec=open("IkesTest.txt","a")
        ipsec=open("/etc/ipsec.secrets","a")
        ipsec.write(newUsername+ " %any%"+ " : "+ "EAP "+newPassword+"\n")
        ipsec.close()

    def fileAddUsers(self, userList):
        pass