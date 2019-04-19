import glob
import importlib
import os

MODULE_EXTENSIONS = ('.py')


class PluginManager():
    def __init__(self):
        self.main_platforms = []
        self.sub_platforms = [] 

    def getAvailablePlugins(self):
        a = os.getcwd()
        print(a)
        os.chdir("/Platforms/MainPlatforms")
        main_platforms = []
        for file in glob.glob("*.py"):
            plugin, ext = file.split(".py")
            main_platforms.append(plugin)
        main_platforms.remove("__init__")
        main_platforms.remove("Platform")
        os.chdir(a)
        os.chdir("./Platforms/Subplatforms")
        sub_platforms = []
        for file in glob.glob("*.py"):
            plugin, ext = file.split(".py")
            sub_platforms.append(plugin)
        main_platforms.remove("__init__")
        main_platforms.remove("Platform")
        os.chdir(a)
        return {"main_platforms": main_platforms, "sub_platforms": sub_platforms}

    def addPlatform(self, path):
        print("cp" + path + " " + ".PlatformManager/Platforms")

    def deletePlatform(self, plugin):
        pluginFile = plugin + ".py"
        os.system("rm " + pluginFile)

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
dictionary = a.getAvailablePlugins()

print(str(dictionary))
