class User:
    def __init__(self, username, password, groupID, internalIP):
        self.username = username
        self.password = password
        self.groupID = groupID
        self.internalIP = internalIP

    
    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, username):
        self.username = username

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.password = password

    @property
    def groupID(self):
        return self.groupID

    @groupID.setter
    def groupID(self, groupID):
        self.groupID = groupID

    @property
    def internalIP(self):
        return self.internalIP

    @internalIP.setter
    def internalIP(self, internalIP):
        self.internalIP = internalIP


    
