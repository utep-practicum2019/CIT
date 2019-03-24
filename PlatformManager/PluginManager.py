import os, sys, importlib, glob
MODULE_EXTENSIONS = ('.py')

class PluginManager():
    
   
    def getAvailablePlugins(self):
        os.chdir("./Platforms")
        platforms = []
        for file in glob.glob("*.py"):
            plugin, ext = file.split(".py")
            platforms.append(plugin)
        platforms.remove("__init__")
        platforms.remove("Platform")
        return platforms  
    
    def addPlatform(self, path):
        print("cp" + path + " " + "./Platforms")
    
    def deletePlatform(self, plugin):
        pluginFile = plugin + ".py"
        os.sys("rm " + pluginFile)
    
    def loadPlatform(self, platform):
        module = importlib.import_module("Platforms." + platform, ".")
        class_ = getattr(module, platform)
        instance = class_()
        return instance

