from ConnectionManager import ConnectionManager

pp = ConnectionManager()
pp.addUsers(1)
pp.pptp_poll_connection()
print("fsafd")
test = pp.update_session_list()
for t in test:
    print(t.username, t.public_ip, t.start_time, t.end_time)
if input() == "stop":
    pp.stop()
print("it worked")
pp.stop()
