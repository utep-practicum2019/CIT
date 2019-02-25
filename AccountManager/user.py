class User(object):
    def __init__(self, username, password, groupID=None, internalIP=None):
        self.username = username
        self.password = password
        self.groupID = groupID
        self.internalIP = internalIP

    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def groupID(self):
        return self._groupID

    @groupID.setter
    def groupID(self, groupID):
        self._groupID = groupID

    @property
    def internalIP(self):
        return self._internalIP

    @internalIP.setter
    def internalIP(self, internalIP):
        self._internalIP = internalIP


    
