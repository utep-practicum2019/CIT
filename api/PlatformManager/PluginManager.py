import glob
import importlib
import os

MODULE_EXTENSIONS = ('.py')


class PluginManager():

    def getAvailablePlugins(self):
        a = os.getcwd()
        os.chdir("./PlatformManager/Platforms")
        platforms = []
        for file in glob.glob("*.py"):
            plugin, ext = file.split(".py")
            platforms.append(plugin)
        platforms.remove("__init__")
        platforms.remove("Platform")
        os.chdir(a)
        return platforms

    def addPlatform(self, path):
        print("cp" + path + " " + ".PlatformManager/Platforms")

    def deletePlatform(self, plugin):
        pluginFile = plugin + ".py"
        os.system("rm " + pluginFile)

    def loadPlatform(self, platform):
        print(platform)
        module = importlib.import_module("PlatformManager.Platforms." + platform, "./")
        # module = importlib.import_module("Platforms." + platform, "./")
        class_ = getattr(module, platform)
        instance = class_()
        return instance  # module = importlib.import_module("PlatformManager.Platforms." + platform, "./")
