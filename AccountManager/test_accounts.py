from account_manager import AccountManager

print('USER MANAGER')
u1 = AccountManager.get_user('user1')
print(repr(u1))
u1s = AccountManager.get_users()
print(repr(u1s))
u1['username'] = 'user3'
print(AccountManager.c)
print

print('GROUP MANAGER')
mygroup = AccountManager.get_group(1)
print('get_group(1) ', repr(mygroup))
groups = AccountManager.get_groups()
print('groups ', repr(groups))
g4 = AccountManager.create_group(4, min_members=4, chatID=4)
