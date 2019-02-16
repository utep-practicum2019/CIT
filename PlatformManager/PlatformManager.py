import sys
import os 
from yapsy.PluginManager import PluginManager

class PlatformManager:
    pluginManager = PluginManager()
    """ 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes

        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """
    
    def __init__(self):
        
        print("Loading plugins")

    def addPlugin(self):
        print("adding plugin")
     
    def removePlugin(self):
        print("removing plugin")

    def configureService(self):
        print("configuring service")
    
    def startService(self):
        print("starting a service")
    
    def stopService(self):
        print("stopping a service")
    
    def showService(self):
        print("showing services")

    def associate_User_Service(self):
        print("Associating a user to a service")
    

platfromManager = PlatformManager()
platfromManager.addPlugin()
platfromManager.removePlugin()
platfromManager.configureService()
platfromManager.showService()
platfromManager.startService()
platfromManager.stopService()
platfromManager.associate_User_Service()

   
