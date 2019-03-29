from ConnectionManager import ConnectionManager

pp = ConnectionManager()
list_of_users = pp.addUsers(3)

for x in list_of_users:
    print (x)
    for u in list_of_users[x]:
        print(u, ':', list_of_users[x][u])

pp.pptp_poll_connection()

print("\nBefore updated session:")
test = pp.update_session_list()


for x in test:
    print (x)
    for u in test[x]:
        print(u, ':', test[x][u])

#for t in test:
#    print(t.username, t.public_ip, t.start_time, t.end_time)

print("After sessions print")

print("finish stopping threads")
pp.stop()

