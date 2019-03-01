import sys
import os 
import abc

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes

        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class PlatformManager(abc.ABC):
    
    @abc.abstractmethod
    def configurePlatform(self):
        pass
    
    @abc.abstractmethod
    def startPlatform(self):
        pass
    
    @abc.abstractmethod
    def stopPlatform(self):
        pass
    




   
