import pyinotify
import subprocess
from .Session import Session
import time
from . import Configure


class EventHandler(pyinotify.ProcessEvent):
    path_to_file = "/var/log"

    def __init__(self, path_to_file, **kargs):
        self.path_to_file = path_to_file

    def process_IN_CREATE(self, event):
        print("Creating:", event.pathname)

    def process_IN_DELETE(self, event):
        print("Removing:", event.pathname)

    def process_IN_MODIFY(self, event):
        if event.pathname == "/var/log/wtmp":
            self.write_PPTPcmd_out()
        print("Modify:", event.pathname)

    def write_PPTPcmd_out(self):
        my_cmd = ['last']
        cmd_out_parser = ['awk', '"/ppp/{print $1,$3,$7,$9,$10,$11}"', '/home/practicum/Desktop/latest/integration/api/PPTP_session_output.txt']

        with open('/home/practicum/Desktop/latest/integration/api/PPTP_session_output.txt', "w") as outfile:
            subprocess.call(my_cmd, stdout=outfile)
        with open('/home/practicum/Desktop/latest/integration/api/PPTP_session.txt', "w") as outfile:
            subprocess.call(cmd_out_parser, stdout=outfile)


class ConnectionManager():
    path_to_file = "/var/log"
    notifier = ""
    isPolling = False

    def __init__(self):
        my_cmd = ['last']
        cmd_out_parser = ['awk', '/ppp/{print $1,$3,$7,$9,$10,$11}', '/home/practicum/Desktop/latest/integration/api/PPTP_session_output.txt']

        with open('/PPTP_session_output.txt', "w") as outfile:
            subprocess.call(my_cmd, stdout=outfile)
        with open('/PPTP_session.txt', "w") as outfile:
            subprocess.call(cmd_out_parser, stdout=outfile)
        pass

    def pptp_poll_connection(self):
        if not self.isPolling:
            wm = pyinotify.WatchManager()  # Watch Manager
            mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY  # flags to determine which events to watch
            handler = EventHandler(self.path_to_file)
            self.notifier = pyinotify.ThreadedNotifier(wm, handler)
            self.isPolling = True
            wdd = wm.add_watch(self.path_to_file, mask, rec=True)
            self.notifier.start()
        else:
            print("Error: polling is already on...")

    def update_session_list(self):
        list_of_sessions = []
        seen = []
        result = []
        index = 0
        with open('/home/practicum/Desktop/latest/integration/api/PPTP_session.txt', "r") as outfile:
            for line in outfile:
                s = line.split()
                # print(s)
                if s[0] not in seen:
                    try:
                        if s[3] == '-':
                            s[4] = "Connected"
                        else:
                            s[4] = "Disconnected"
                    except IndexError:
                        s[3] = "Reset"
                        s.append("Disconnected")

                    list_of_sessions.append({
                        "username": s[0],
                        "public_ip": s[1],
                        "start_end": s[2],
                        "end_time": s[3],
                        "status": s[4],
                        "connection_type": "PPTP"}
                    )
                    seen.append(s[0])

        return list_of_sessions

    def stop(self):
        if self.isPolling:
            self.isPolling = False
            self.notifier.stop()
        else:
            print("Error: polling is already off...")

    def addUsers(self, numberOfUsers):
        usersArr = []
        usersArr = Configure.addUsers(numberOfUsers)
        usersDictionary = {}
        for x in range(numberOfUsers):
            usersDictionary[x] = {"username":usersArr[x].username,
            "password":usersArr[x].password,"pptpIP":usersArr[x].pptpIP}
        return usersDictionary

    def deleteUsers(self,listOfUsers):
        deleteResult=Configure.deleteUsers(listOfUsers)
        return deleteResult

    def updateUserConnection(self, currUsername,newUsername,newPassword,newIP):
        updateResult=Configure.modifyUser(currUsername,newUsername,newPassword,newIP)
        return updateResult

    def fileAddUsers(self, userList):
        usersArr=[]
        usersArr=Configure.fileAddUsers(userList)
        usersDictionary={}
        for x in range(len(userList)):
            usersDictionary[x] = {"username":usersArr[x].username,
            "password":usersArr[x].password,"pptpIP":usersArr[x].pptpIP}
        return usersDictionary

"""
if __name__ == "__main__":
    pp = ConnectionManager()
    l = pp.update_session_list()
    for li in l:
        print(li)

    pp = ConnectionManager()
    pp.pptp_poll_connection()
    pp.pptp_poll_connection()

    while True:
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            pp.stop()
            pp.stop()
            pp.stop()
            break
        except:
            pp.stop()
            pp.stop()
            raise
    pp.pptp_poll_connection()
    pp.pptp_poll_connection()
    pp.stop()




last = /var/log/wtmp
who  = /var/run/utmp
last = /var/log/btmp
"""
"""
last = /var/log/wtmp
who  = /var/run/utmp
last = /var/log/btmp
"""
