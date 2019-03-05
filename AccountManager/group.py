import json

class Group:
    def __init__(self, group_id, min_members=None, max_members=None, platforms=None, members=None, chat_id=None):
        if min_members is not None: self.min_members = min_members
        if max_members is not None: self.max_members = max_members
        if platforms is not None: self.platforms = platforms
        if chat_id is not None: self.chat_id = chat_id
        if members is not None:
            self.members = members
        else:
            self.members = []
        self.group_id = group_id


    def __repr__(self):
        tmp = "Group("
        my_vars = vars(self)
        for v in my_vars.keys():
            tmp += '%r=%r, ' %(v, my_vars[v])
        return tmp[:-2] + ")"

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        self._group_id = group_id

    @property
    def min_members(self):
        try:
            return self._min_members
        except AttributeError:
            return None

    @min_members.setter
    def min_members(self, min_members):
        self._min_members = min_members

    @property
    def max_members(self):
        try:
            return self._max_members
        except AttributeError:
            return None

    @max_members.setter
    def max_members(self, max_members):
        self._max_members = max_members

    @property
    def platforms(self):
        try:
            return self._platforms
        except AttributeError:
            return None

    @platforms.setter
    def platforms(self, platforms):
        self._platforms = platforms

    @property
    def members(self):
        try:
            return self._members
        except AttributeError:
            return None

    @members.setter
    def members(self, members):
        self._members = members

    @property
    def chat_id(self):
        try:
            return self._chat_id
        except AttributeError:
            return None

    @chat_id.setter
    def chat_id(self, chat_id):
        self._chat_id = chat_id

    def toJSON(self):
        clean_vars = {}
        my_vars = vars(self)
        for v in my_vars.keys():
            # remove underscore from properties
            clean_vars[v[1:]] = my_vars[v]
        return json.dumps(clean_vars)
