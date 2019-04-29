from .Platform import Platform
import subprocess

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class is a subclass of platform. This class will implement the tiddlywiki platform. 
    """

class VirtualMachine(Platform):
    # fill the values here for your specific platform
    platform_name = "IDS Virtual Machine"
    platform_alias = ""
    platform_note = ""
    platform_start_command = "sudo su - practicum -c 'VBoxManage startvm Ubuntu16 --type headless'"
    platform_end_command = "sudo su - practicum -c 'VBoxManage controlvm Ubuntu16 poweroff'"
    platform_version = ""
    platformInstallation = " "
    port = "0"
    ip = "0.0.0.0"
    link = "submission.com"

    # the fields below will be generated by Platform Manager
    processID = 0
    platform_id = 0
    subplatforms = {" ", " "}
    staticPlatform = False 
    
    #return process ID
    def getProcessID(self):
        return self.processID

    #returns link to connect to website
    def getLink(self):
        return self.link

    #returns ip and port to connect to website
    def getIpPort(self):
        return self.ip + ":" + self.port

    #returns platform name
    def getPlatformName(self):
        return self.platform_name

    #returns platform alias
    def getPlatformAlias(self):
        return self.platform_alias

    #returns platform note
    def getPlatformNote(self):
        return self.platform_note

    #returns where the platforms installation path
    def getPlatformInstallation(self):
        return self.platformInstallation

    #return the version of the platform
    def getPlatformVersion(self):
        return self.platform_version

    #return a platformID. You can pick a random value for this field.
    def getPlatformID(self):
        return int(self.platform_id)

    #return command that starts platform
    def get_start_command(self):
        process = subprocess.Popen(['vboxmanage showvminfo Ubuntu16 | grep -c "running (since"'], shell=True, stdout=subprocess.PIPE)
        out, err = process.communicate()
        #print(out.decode("utf-8"))
        if "0" in out.decode("utf-8"):
            self.platform_start_command = "sudo su - practicum -c 'VBoxManage startvm Ubuntu16 --type headless'"
        else:
            self.platform_start_command = "sleep 5"
        return self.platform_start_command

    #returns command to stop platform
    def get_stop_command(self):
        return self.platform_end_command

    #returns list of subplatforms
    def get_sub_platforms(self):
        return self.subplatforms

    #sets process ID
    def setProcessID(self, processID):
        self.processID = processID

    #set link to connect to website
    def setLink(self, link):
        self.link = link

    #set ip and port to connect to website
    def setIpPort(self, ip, port):
        self.ip = ip
        self.port = port

    #set platform name
    def setPlatformName(self, platform_name):
        self.platform_name = platform_name

    #set platform alias
    def setPlatformAlias(self, alias):
        self.platform_alias = alias 

    #set platform note
    def setPlatformNote(self, note):
        self.platform_note = note

    #set where the platforms installation path
    def setPlatformInstallation(self, platformInstallation):
        self.platformInstallation = platformInstallation

    #sets the version of the platform
    def setPlatformVersion(self, platform_version):
        self.platform_version = platform_version

    #sets a platformID. You can pick a random value for this field.
    def setPlatformID(self, PlatformID):
        self.platform_id = PlatformID

    #sets command that starts platform
    def set_start_command(self, platform_start_command):
        self.platform_start_command = platform_start_command

    #set command to stop platform
    def set_stop_command(self, platform_end_command):
        self.platform_end_command = platform_end_command

    #set list of subplatforms
    def set_sub_platforms(self, subplatforms):
        self.subplatforms = subplatforms

    def requestHandler(self, command):
        action = {
            'checkvmstatus': self.check_vm_status,
            'startvm': self.start_vm,
            'startvmscenario': self.start_vm_scenario,
            'stopvm': self.stop_vm
        }
        return action[command['command']](command['param'])
    
    #add more methods below if you need to do more tasks

    def check_vm_status(self, param):

        result = {'status': False}
        out = self.vm_command(["vboxmanage showvminfo Ubuntu16 | grep -c 'running (since'"])
        if "0" in out:
            result['status'] = False
        else:
            result['status'] = True
        return result

    def start_vm_scenario(self, param):
        result = {'running': False}
        out = self.vm_command(["VBoxManage guestcontrol 'Ubuntu16' -v --username hackathon --password toor run --exe '/usr/bin/python3' --no-wait-stderr --no-wait-stdout -- /home/hackathon/" + param['filename']])
        print(out)
        if "successfully terminated" in out:
            result['running'] = True
        else:
            result['running'] = False
        return result

    def start_vm(self, param):
        result = {'running': False}
        out = self.vm_command(["VBoxManage startvm 'Ubuntu16' --type headless"])
        print(out)
        if "successfully" in out:
            result['running'] = True
        else:
            result['running'] = False
        return result

    def stop_vm(self, param):
        result = {'stopped': False}
        out = self.vm_command(['VBoxManage controlvm "Ubuntu16" poweroff'])
        # out = self.vm_command(['VBoxManage snapshot Ubuntu16 restore "OnStartupCallsWorking"'])
        print(out)
        if "Restoring snapshot" in out:
            result['stopped'] = True
        else:
            result['stopped'] = False
        return result

    def vm_command(self, cmd):
        process = subprocess.Popen("su - practicum -c '" + cmd[0] + "'", shell=True, stdout=subprocess.PIPE)
        out, err = process.communicate()
        return out.decode("utf-8")


"""
platform = VirtualMachine()
print(platform.get_start_command())
cmd = {
    'command' : 'stopvm',
    'param': 'filename.txt'
}
r = platform.requestHandler(cmd)

print(r)

"""