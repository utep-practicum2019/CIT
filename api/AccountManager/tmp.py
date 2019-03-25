# from AccountManager.user import User
# from AccountManager.group import Group
#
#     @staticmethod
#     def get_users():
#         doc_data = {'collection_name':'users'}
#         users = requests.get(UserManager.database_url, json=doc_data)
#         return users.json()
#
#     @staticmethod
#     def get_groups():
#         r = requests.get(GroupManager.database_url)
#         if r.status_code == requests.codes.ok:
#             groups_js = r.json()
#             return groups_js
#         return False
#
#     @staticmethod
#     def detach_platform(platform_name):
#         cursor = Database.collection['groups'].find({'platforms': platform_name})
#         while True:
#             groups = []
#             try:
#                 current = cursor.next()
#                 print(repr(current))
#                 current['platforms'].remove(platform_name)
#                 print(repr(current))
#                 groups.append(current['group_id'])
#             except StopIteration:
#                 return True
#             except KeyError:
#                 return False
#
#
# file_content = [
#     "user01 user02 user03\n",
#     "user04 user05\n"
# ]
# start_id = 0
# group_count = 2
# connection_url = 'http://127.0.0.1:5000/api/v2/resources/connection'
# test_filepath = 'tmp.txt'
# group_id_filepath = 'next_group_id.txt'
# from AccountManager.group_manager import GroupManager, get_next_id
# with open(test_filepath, 'w') as f:
#     f.writelines(file_content)
# start_id = get_next_id()
# GroupManager.create_groups(filepath=test_filepath)

