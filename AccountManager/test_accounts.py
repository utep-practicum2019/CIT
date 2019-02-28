from user import User
from user_manager import UserManager
from group import Group
from group_manager import GroupManager
from database import Database
"""
print("USERS")
u1 = User('user1', 'pass1', 1, 'ip1')
u2 = User('name2', 'pass2')
print(repr(u1))
print(repr(u2))

print("GROUPS")
g1 = Group(1)
g2 = Group(2, 3, 4, None, [u2, u1], 2)
print(repr(g1))
print(repr(g2))
"""
u1 = UserManager.get_user("user1")
print(repr(u1))
us = UserManager.get_users()
print(repr(us))

"""
print("GROUP MANAGER")
mygroup = GroupManager.get_group(1)
print("get_group(1) ", repr(mygroup))
groups = GroupManager.get_groups()
print("groups ", repr(groups))
g4 = GroupManager.create_group(4, min_members=4, chatID=4)
"""
