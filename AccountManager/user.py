class User(object):
    def __init__(self, username, password, group_id=None, internal_ip=None):
        self.username = username
        self.password = password
        self.group_id = group_id
        self.internal_ip = internal_ip

    def __repr__(self):
        str = "User(user=%r, password=%r" % (self.username, self.password)
        if self.group_id is not None:
            str += ", group_id=%r" % (self.group_id)
        if self.internal_ip is not None:
            str += ", internal_ip=%r" % (self.internal_ip)
        str += ")"
        return str
    
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
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        self._group_id = group_id

    @property
    def internal_ip(self):
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        self._internal_ip = internal_ip


    
