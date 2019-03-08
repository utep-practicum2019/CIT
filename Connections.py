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
