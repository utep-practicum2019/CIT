from ConnectionManager import ConnectionManager

pp = ConnectionManager()
pp.addUsers(1)
pp.poll_connection()
print("fsafd")
pp.update_session_list()
if input() == "stop":
    pp.stop()
print("it worked")
pp.stop()
