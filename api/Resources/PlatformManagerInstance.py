from PlatformManager.PlatformInterface import PlatformInterface


class PlatformManagerInstance:
    __instance = None

    @staticmethod
    def get_instance():
        # Static access method 
        if PlatformManagerInstance.__instance is None:
            PlatformManagerInstance()
        return PlatformManagerInstance.__instance

    def __init__(self):
        # Private constructor
        if PlatformManagerInstance.__instance is not None:
            raise Exception("Singleton Class!")
        else:
            self.platform_interface = PlatformInterface()
            PlatformManagerInstance.__instance = self
