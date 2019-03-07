from ConnectionManager import ConnectionManager

pp = ConnectionManager()
list_of_users = pp.addUsers(3)

for x in list_of_users:
    print (x)
    for u in list_of_users[x]:
        print(u,':',list_of_users[x][u])

pp.pptp_poll_connection()
print("fsafd")
test = pp.update_session_list()
for t in test:
    print(t.username, t.public_ip, t.start_time, t.end_time)
if input() == "stop":
    pp.stop()
print("it worked")
pp.stop()
