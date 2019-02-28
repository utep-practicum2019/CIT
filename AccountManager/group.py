
class Group:
    def __init__(self, group_id, min_members=None, max_members=None, platforms=None, members=None, chat_id=None):
        self.group_id = group_id
        self.min_members = min_members
        self.max_members = max_members
        self.platforms = platforms
        self.members = members
        self.chat_id = chat_id

    def __repr__(self):
        str = "Group(group_id=%r" % (self.group_id)
        if self.min_members is not None:
            str += ", min_members=%r" % (self.min_members)
        if self.max_members is not None:
            str += ", max_members=%r" % (self.max_members)
        if self.platforms is not None:
            str += ", platforms=%r" % (self.platforms)
        if self.members is not None:
            str += ", members=%r" % (self.members)
        if self.chat_id is not None:
            str += ", chat_id=%r" % (self.chat_id)
        return str + ")"

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        self._group_id = group_id

    @property
    def min_members(self):
        return self._min_members

    @min_members.setter
    def min_members(self, min_members):
        self._min_members = min_members

    @property
    def max_members(self):
        return self._max_members

    @max_members.setter
    def max_members(self, max_members):
        self._max_members = max_members

    @property
    def platforms(self):
        return self._platforms

    @platforms.setter
    def platforms(self, platforms):
        self._platforms = platforms

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, members):
        self._members = members

    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        self._chat_id = chat_id

