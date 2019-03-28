from PlatformManager.PlatformInterface import PlatformInterface


class PlatformManagerInstance:
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method 
        if PlatformManagerInstance.__instance == None:
            PlatformManagerInstance()
        return PlatformManagerInstance.__instance

    def __init__(self):
        # Private constructor
        if PlatformManagerInstance.__instance != None:
            raise Exception("Singleton Class!")
        else:
            self.platform_interface = PlatformInterface()
            PlatformManagerInstance.__instance = self
