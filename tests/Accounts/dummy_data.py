user1 = {
    'username': 'user001',
    'password': 'pass1',
    'group_id': 1,
    'internal_ip': '127.0.0.11',
    'remote_ip': '127.0.0.111',
    'connection_type': 'PPTP'
}

updated_user1 = {
    'username': 'user001',
    'password': 'updated',
    'group_id': 2,
    'internal_ip': '127.0.0.12',
    'remote_ip': '127.0.0.112',
    'connection_type': 'IKEv2'
}

user2 = {
    'username': 'user002',
    'password': 'pass2',
    'group_id': 1,
    'internal_ip': '127.0.0.12',
    'remote_ip': '127.0.0.122',
    'connection_type': 'PPTP'
}

bare_user = {
    'username': 'bare_user',
    'password': 'pass1'
}

updated_group = {
    'group_id': 101,
    'min': 3,
    'max': 4,
    'chat_id': 111
}

users = [
    ['user001', 'pass1', '127.0.0.1'],
    ['user002', 'pass2', '127.0.0.1'],
    ['user003', 'pass3', '127.0.0.1']
]

"""
    ---- file_content constraints ----
    must have at least two strings
    must have a newline at the end of each string
    must not have empty strings
"""
file_content = [
    "user01 user02 user03\n",
    "user04 user05\n"
]

file_users = [line.strip().split() for line in file_content]

start_id = 0
group_count = 2
user_count = 3
connection_url = 'http://127.0.0.1:5000/api/v2/resources/connection'
test_filepath = 'tmp.txt'

