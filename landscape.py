#!/usr/bin/env python.

"""
    This file defines the landscapes

"""

import random
import unittest
from landscapeTypes import LandscapeTypes
from standardNames import StandardNames

__author__ = "Sven Eggert"
__copyright__ = "Copyright 2017, Egertiko Designs"
__credits__ = []
__license__ = "GPL"
__version__ = "0.0.9"
__maintainer__ = "Sven Eggert"
__email__ = "sven674@web.de"
__status__ = "Development"

"""

    The Landscape class

"""
class Landscape(unittest.TestCase):
    landscapeWidth = 284            # width of the landscape e.g. miles
    landscapeHeight = 284
    tileWidth = 1                   # width of one tile in miles
    tileHeight = 1
    
    MAX_SIZE_AREA = 50.0
    MIN_SIZE_ARE = 5.0
    
    MAX_ANGLE_AREA = 90.0
    MIN_ANGLE_AREA = 0.0

    landscapeNames = {LandscapeTypes.FOREST : ['Shire', 'Forest', 'Wood', 'Copse', 'Timber', 'Thicket', 'Woodland', 'Timberland', 'Backwoods'], \
                      LandscapeTypes.MOUNTAIN : ['Mountain', 'Cliff', 'Peak', 'Ridge', 'Sierra', 'Alp', 'Mount', 'Pike', 'Range'], \
                      LandscapeTypes.LAKE : ['Lake', 'Pool', 'Pond', 'Creek', 'Lagoon', 'Reservoir', 'Spring', 'Mouth', 'Cistern'], \
                      LandscapeTypes.HILL : ['Hill', 'Slope'], \
                      LandscapeTypes.FORTRESS : ['Fortress', 'Citadel', 'Fortification', 'Castle', 'Fort'], \
                      LandscapeTypes.CITY : ['City', 'Municipal'], \
                      LandscapeTypes.KEEP : ['Keep', 'Refuge'], \
                      LandscapeTypes.PALACE : ['Palace', 'Hall', 'Manor', 'Mansion', 'Residence', 'Chateau', 'Dwelling'], \
                      LandscapeTypes.TOWER : ['Tower', 'Lookout'], \
                      LandscapeTypes.RUINS : ['Ruins', 'Remains', 'Debris', 'Relics'], \
                      LandscapeTypes.DESERT : ['Desert', 'Desolation', 'Lonely', 'Waste'], \
                      LandscapeTypes.MEADOW : ['Meadow', 'Grassland', 'Pasture', 'Prairie', 'Grassland', 'Grass'], \
                      LandscapeTypes.SWAMP  : ['Swamp', 'Mould', 'Moor', 'Morass', 'Mud', 'Bog'], \
                      LandscapeTypes.HILL   : ['Hill', 'Highland', 'Hillside', 'Hilltop', 'Ridge', 'Slope', 'Cliff', 'Mound'], \
                      LandscapeTypes.SANDS : ['Sand', 'Dune']}

    """
        Create a random landscap ename
    """
    def createName(self, landscape, positiveness):
        landscapeName = random.choice(self.landscapeNames[landscape])
        selector = random.random()
        usePlural = False  # do not use the plural
    
        if selector < 0.5:
             # Element
            additionalName = random.choice(StandardNames.elementNames)
            if additionalName[1]:
                usePlural = True   # for the elements the plural sounds better
            additionalName = additionalName[0]
        elif selector < 0.7:
            # Bird
            additionalName = random.choice(StandardNames.birdNamesFirstPart)
            usePlural = True   # for the birds the plural sounds better
        else:
            if random.random() < positiveness:
                # choose positive names
                additionalName = random.choice(StandardNames.positiveNames)
            else:
                # choose negative names
                additionalName = random.choice(StandardNames.negativeNames)

        if random.random() < 0.5:
            landscapeName += " of " + additionalName.title()
            if usePlural:
                landscapeName += "s"
        else:
            landscapeName = additionalName + "-" + landscapeName.title() 

        return landscapeName


    """
        Create a random name for a forest
    """
    def createForestName(self, positiveness):
        forestName = self.createName(LandscapeTypes.FOREST, positiveness)
 
        return forestName

    """
        Create a random name for a mountain
        
    """
    def createMountainName(self, positiveness):
        mountainName = self.createName(LandscapeTypes.MOUNTAIN, positiveness)
 
        return mountainName

    """
        Create a random name for a swamp
    """
    def createSwampName(self, positiveness):
        swampName = self.createName(LandscapeTypes.SWAMP, positiveness)
 
        return swampName

    """

        Test forest names

    """
    def test_createForest(self,):
        forest = Landscape()
        x = 100
        while x > 0:
          print (forest.createForestName(random.random()))
          x = x - 1
      
    """

        Test swamp names

    """
    def test_createSwamp(self):
        swamp = Landscape()
        x = 100
        while x > 0:
          print(swamp.createSwampName(random.random()))
          x = x - 1  

    """
        Test create mountain names
    """
    def test_createMountain(self):
        mountain = Landscape()
        x = 100
        while x > 0:
          print (mountain.createMountainName(random.random()))
          x = x - 1

if __name__ == '__main__':
    unittest.main()
