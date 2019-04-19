import glob
import importlib
import os

MODULE_EXTENSIONS = ('.py')


class PluginManager():

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
        try:
            print(platform)
            # module = importlib.import_module("PlatformManager.Platforms." + platform, "./")
            module = importlib.import_module("Platforms.Main_Platforms." + platform, "./")
            class_ = getattr(module, platform)
            instance = class_()
            return instance  # module = importlib.import_module("PlatformManager.Platforms." + platform, "./")
        except:
            module = importlib.import_module("Platforms.Sub_platforms." + platform, "./")
            class_ = getattr(module, platform)
            instance = class_()
            return instance  # module = importlib.import_module("PlatformManager.Platforms." + platform, "./")

a = PluginManager()
dictionary = a.getAvailablePlugins()

print(str(dictionary))