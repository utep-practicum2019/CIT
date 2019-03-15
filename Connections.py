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
        currUserCounter=0
        currIP_END_Counter=0
        with open(secretsFile) as read:
            for currLine in read:
                if(currLine[0][0]!='#' and currLine[0][0] != '1' and currLine[0][0] != '\n'):
                    currUserCounter+=1
                    currIP_END_Counter+=1
        userNumVar=1+currUserCounter
        # print(userNumVar)
        ipEND=2+currIP_END_Counter
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
        configFile=open(fileName,"r+")
        configTempFile=open(tempFile,"r+")
        configFile.truncate(0)
        with configTempFile as oldfile, configFile as newfile:
            for line in oldfile:
                newfile.write(line)
        configTempFile=open(tempFile,"r+")
        configTempFile.truncate(0)

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
        
        # ipsec=open("IkesTest.txt","a")
        ipsec=open("/etc/ipsec.secrets","a")
        ipsec.write(newUsername+ " %any%"+ " : "+ "EAP "+newPassword+"\n")