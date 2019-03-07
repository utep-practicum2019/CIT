import pyinotify
import subprocess
from Session import Session
import time
import Configure


class EventHandler(pyinotify.ProcessEvent):
    path_to_file = "/var/log"

    def __init__(self, path_to_file):
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
        cmd_out_parser = ['awk', '/ppp/{print $1,$3,$7,$9,$10,$11}', 'PPTP_session_output.txt']

        with open('PPTP_session_output.txt', "w") as outfile:
            subprocess.call(my_cmd, stdout=outfile)
        with open('PPTP_session.txt', "w") as outfile:
            subprocess.call(cmd_out_parser, stdout=outfile)


class ConnectionManager():
    path_to_file = "/var/log"
    notifier = ""

    def __init__(self):
        pass

    def pptp_poll_connection(self):
        wm = pyinotify.WatchManager()  # Watch Manager
        mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY  # flags to determine which events to watch
        handler = EventHandler(self.path_to_file)
        self.notifier = pyinotify.ThreadedNotifier(wm, handler)
        wdd = wm.add_watch(self.path_to_file, mask, rec=True)
        self.notifier.start()

    def update_session_list(self):
        list_of_sessions = []
        with open('PPTP_session.txt', "r") as outfile:
            for line in outfile:
                s = line.split()
                list_of_sessions.append(Session(s[0], s[1], s[2], s[3], s[4], "PPTP"))
        return list_of_sessions

    def stop(self):
        self.notifier.stop()

    def addUsers(self,numberOfUsers):
        usersArr=[]
        usersArr=Configure.addUsers(numberOfUsers)
        usersDictionary={}
        for x in range(numberOfUsers):
            usersDictionary[x]=[usersArr[x].username,usersArr[x].password,usersArr[x].pptpIP]

        return usersArr

"""
if __name__ == "__main__":
    pp = ConnectionManager("/var/log")
    nn = pp.notifier

    while True:
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            nn.stop()
            break
        except:
            nn.stop()
            raise
            
"""         
"""
last = /var/log/wtmp
who  = /var/run/utmp
last = /var/log/btmp
"""
"""
last = /var/log/wtmp
who  = /var/run/utmp
last = /var/log/btmp
"""
