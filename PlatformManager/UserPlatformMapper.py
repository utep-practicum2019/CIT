import sys
import os
from yapsy.PluginManager import PluginManager
import abc


""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platform manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class UserPlatformMapper():
    def __init__(self):
        self.var_a = None

