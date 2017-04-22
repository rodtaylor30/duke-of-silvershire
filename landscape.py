import random
import unittest
from landscapeTypes import LandscapeTypes

class Landscape:
    landscapeWidth = 284.29         # e.g. miles
    landscapeHeight = 284.29
    tileWidth = 1                   # width of one tile 
    tileHeight = 1
    
    MAX_SIZE_AREA = 50.0
    MIN_SIZE_ARE = 5.0
    
    MAX_ANGLE_AREA = 90.0
    MIN_ANGLE_AREA = 0.0

    landscapeNames = {LandscapeTypes.FOREST : ['Shire', 'Forest', 'Wood', 'Copse', 'Timber', 'Thicket', 'Woodland', 'Timberland', 'Backwoods'], \
                      LandscapeTypes.SWAMP  : ['Swamp', 'Mould', 'Moor', 'Morass', 'Mud']}

"""
    Create a random name for a forest
"""
    def createForestName(self):
        forestName = random.choice(self.landscapeNames[LandscapeTypes.FOREST])
        forestName += " of "

        return forestName

"""
    Create a random name for a swamp
"""
    def createSwampName(self):
        swampName = random.choice(self.landscapeNames[LandscapeTypes.FOREST])
        swampName += " of "

        return swampName

