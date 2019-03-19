from AccountManager.user import User
from AccountManager.group import Group

try:
    freader = open('next_group_id', 'r')
    freader.close()
except FileNotFoundError:
    fwriter = open('next_group_id', 'w')
    fwriter.write('1')

for i in range(3):
    freader = open('next_group_id', 'r')
    group_id = int(freader.readline())
    print(group_id)
    freader.close()
    if group_id is not None:
        group = Group(group_id)
        for j in range(4):
            # call to Connections
            username = 'user' + str(j) + "G" + str(group_id)
            password = "pass1"
            remote_ip = "127.0.0.1" + str(i) + str(j)
            user = User(username, password, remote_ip)
            group.members.append(username)
            # TODO: Store user in database
            print(repr(user))
        # TODO: Store group in database
        print(repr(group))
    fwriter = open('next_group_id', 'w')
    fwriter.write(str(group_id + 1))
    fwriter.close()

    @staticmethod
    def get_users():
        doc_data = {'collection_name':'users'}
        users = requests.get(UserManager.database_url, json=doc_data)
        return users.json()

    @staticmethod
    def get_groups():
        r = requests.get(GroupManager.database_url)
        if r.status_code == requests.codes.ok:
            groups_js = r.json()
            return groups_js
        return False
