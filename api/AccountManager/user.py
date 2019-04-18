class User(object):
    def __init__(self, username, password=None, group_id=None, internal_ip=None, remote_ip=None, connection_type=None):
        self.username = username
        if password is not None:
            self.password = password
        if group_id is not None:
            self.group_id = group_id
        if internal_ip is not None:
            self.internal_ip = internal_ip
        if remote_ip is not None:
            self.remote_ip = remote_ip
        if connection_type is not None:
            self.connection_type = connection_type

    def __repr__(self):
        tmp = "User("
        my_vars = vars(self)
        for v in my_vars.keys():
            tmp += '%r=%r, ' % (v, my_vars[v])
        return tmp[:-2] + ")"

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        try:
            return self._password
        except AttributeError:
            return None

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def group_id(self):
        try:
            return self._group_id
        except AttributeError:
            return None

    @group_id.setter
    def group_id(self, group_id):
        self._group_id = group_id

    @property
    def internal_ip(self):
        try:
            return self._internal_ip
        except AttributeError:
            return None

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        self._internal_ip = internal_ip

    @property
    def remote_ip(self):
        try:
            return self._remote_ip
        except AttributeError:
            return None

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        self._remote_ip = remote_ip

    @property
    def connection_type(self):
        try:
            return self._connection_type
        except AttributeError:
            return None

    @connection_type.setter
    def connection_type(self, connection_type):
        self._connection_type = connection_type

    @property
    def notes(self):
        try:
            return self._notes
        except AttributeError:
            return ""

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @property
    def alias(self):
        try:
            return self._alias
        except AttributeError:
            return ""

    @alias.setter
    def alias(self, alias):
        self._alias = alias

    def to_dict(self):
        clean_vars = {}
        my_vars = vars(self)
        for v in my_vars.keys():
            # remove underscore from properties
            clean_vars[v[1:]] = my_vars[v]
        return clean_vars
