import os, sys

class PluginManager():
    platforms = {"tiddly wiki","rocket chat"}
    
    def get_Available_Platforms(self):
        return self.platforms
    
    def addPlatform(self):
        print("Adding Platforms")
    
    def deletePlatform(self):
        print("Deleting platforms")
    
    def loadPlatform(self):
        print("Instantiating objects")

    