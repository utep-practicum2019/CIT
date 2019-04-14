class Group:
    def __init__(self, group_id, min=None, max=None, platforms=None, members=None, chat_id=None):
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if chat_id is not None:
            self.chat_id = chat_id
        if platforms is not None:
            self.platforms = platforms
        else:
            self.platforms = []
        if members is not None:
            self.members = members
        else:
            self.members = []
        self.group_id = group_id

    def __repr__(self):
        tmp = "Group("
        my_vars = vars(self)
        for v in my_vars.keys():
            tmp += '%r=%r, ' % (v, my_vars[v])
        return tmp[:-2] + ")"


    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        self._group_id = group_id

    @property
    def min(self):
        try:
            return self._min
        except AttributeError:
            return None

    @min.setter
    def min(self, min):
        self._min = min

    @property
    def max(self):
        try:
            return self._max
        except AttributeError:
            return None

    @max.setter
    def max(self, max):
        self._max = max

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

    def to_dict(self):
        clean_vars = {}
        my_vars = vars(self)
        for v in my_vars.keys():
            # remove underscore from properties
            clean_vars[v[1:]] = my_vars[v]
        return clean_vars
