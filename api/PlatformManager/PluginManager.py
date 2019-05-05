import glob
import importlib
import os
from shutil import *

MODULE_EXTENSIONS = ('.py')


class PluginManager():
    def __init__(self):
        self.main_platforms = []
        self.sub_platforms = []
        self.pluginsPath =  "Platforms/"

    def getAvailablePlugins(self):
        original_wd = os.getcwd()
        print(original_wd)
        os.chdir("PlatformManager/Platforms/MainPlatforms")
        main_platforms = []
        for file in glob.glob("*.py"):
            plugin, ext = file.split(".py")
            main_platforms.append(plugin)
        if "__init__" in main_platforms:
            main_platforms.remove("__init__")
        if "Platform" in main_platforms:
            main_platforms.remove("Platform")
        os.chdir(original_wd)
        os.chdir("PlatformManager/Platforms/SubPlatforms")
        sub_platforms = []
        for file in glob.glob("*.py"):
            plugin, ext = file.split(".py")
            sub_platforms.append(plugin)
        if "__init__" in sub_platforms:
            sub_platforms.remove("__init__")
        if "Platform" in sub_platforms:
            sub_platforms.remove("Platform")
        os.chdir(original_wd)
        return {"main_platforms": main_platforms, "sub_platforms": sub_platforms}

    def addPlatform(self, path, pluginType):
        try:
            if(pluginType == "main"):
                 copy(path, self.pluginsPath + "MainPlatforms")
            else:
                copy(path, self.pluginsPath + "SubPlatforms")
            return True
        except:
            print("Plugin Import Failed")
            return False
    def deletePlatform(self, plugin, pluginType):
        # try:
            original_wd = os.getcwd()
            if(pluginType == "main"):
                os.chdir(self.pluginsPath + "MainPlatforms")
                # os.chdir("PlatformManager/Platforms/MainPlatforms")
                pluginFile = plugin + ".py"
                os.remove(pluginFile)
            else:
                os.chdir(self.pluginsPath + "SubPlatforms")
                # os.chdir("PlatformManager/Platforms/SubPlatforms")
                pluginFile = plugin + ".py"
                os.remove(pluginFile)
            os.chdir(original_wd)

            return True
        # except e:
        #     print("File not found. Deletion Failure")
        #     return False 

    def loadPlatform(self, platform):
        print(platform)
        try:
            module = importlib.import_module("PlatformManager.Platforms.MainPlatforms." + platform, "./")
            # module = importlib.import_module("Platforms." + platform, "./")
            class_ = getattr(module, platform)
            instance = class_()
            return instance  # module = importlib.import_module("PlatformManager.Platforms." + platform, "./")
        except Exception as e:
            module = importlib.import_module("PlatformManager.Platforms.SubPlatforms." + platform, "./")
            # module = importlib.import_module("Platforms." + platform, "./")
            class_ = getattr(module, platform)
            instance = class_()
            return instance  # module = importlib.import_module("PlatformManager.Platforms." + platform, "./")


a = PluginManager()
a.addPlatform("/home/osboxes/Desktop/main1.py", "main")
a.addPlatform("/home/osboxes/Desktop/sub1.py", "sub")
b = raw_input()
a.deletePlatform("main1", "main")
a.deletePlatform("sub1", "sub")
