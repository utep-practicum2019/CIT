import glob
import importlib
import os

MODULE_EXTENSIONS = ('.py')


class PluginManager():
    def __init__(self):
        self.main_platforms = []
        self.sub_platforms = []

    def getAvailablePlugins(self):
        original_wd = os.getcwd()
        # print(original_wd)
        # os.chdir("Platforms/MainPlatforms")
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
        # os.chdir("Platforms/SubPlatforms")
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

    # need to work on
    def addPlatform(self, path):
        print("cp" + path + " " + ".PlatformManager/Platforms")

    # need to work on
    def deletePlatform(self, plugin):
        pluginFile = plugin + ".py"
        os.system("rm " + pluginFile)

    def loadPlatform(self, platform):
        # print(platform)
        try:
            module = importlib.import_module("PlatformManager.Platforms.MainPlatforms." + platform, "./")
            # module = importlib.import_module("Platforms.MainPlatforms." + platform, "./")
            class_ = getattr(module, platform)
            instance = class_()
            return instance  # module = importlib.import_module("PlatformManager.Platforms." + platform, "./")
        except Exception as e:
            module = importlib.import_module("PlatformManager.Platforms.SubPlatforms." + platform, "./")
            # module = importlib.import_module("Platforms.SubPlatforms." + platform, "./")
            class_ = getattr(module, platform)
            instance = class_()
            return instance  # module = importlib.import_module("PlatformManager.Platforms." + platform, "./")
