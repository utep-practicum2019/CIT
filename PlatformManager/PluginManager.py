import os, sys
import importlib


class PluginManager():
    
    def get_Available_Platforms(self):
        return 0
    
    def addPlatform(self):
        print("Adding Platforms")
    
    def deletePlatform(self):
        print("Deleting platforms")
    
    def loadPlatform(self, platform):
        module = importlib.import_module("Platforms." + platform, ".")
        class_ = getattr(module, platform)
        instance = class_()
        return instance




    