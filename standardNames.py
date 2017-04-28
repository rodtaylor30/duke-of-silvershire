#!/usr/bin/env python.

"""
    This file defines the standard names of the game

"""

import unittest

__author__ = "Sven Eggert"
__copyright__ = "Copyright 2017, Egertiko Designs"
__credits__ = []
__license__ = "GPL"
__version__ = "0.0.9"
__maintainer__ = "Sven Eggert"
__email__ = "sven674@web.de"
__status__ = "Development"

"""
    The class contains all standard names
"""
class StandardNames(unittest.TestCase):
    negativeNames = ['Misery', 'Misfortune', 'Mist', 'Mite', 'Mockery', 'Moisture', 'Shadow', 'Fire', 'Ghost', 'Twilight', 'Whisper', 'Murmur', 'Morgue', \
                     'Mortality', 'Mortuary', 'Muck', 'Mystery', 'Nausea', 'Night', 'Nightfall', 'Nighttime', 'Nightmare', 'Numbness', 'Oath', 'Obliteration', \
                     'Obscurity', 'Obstacles', 'Occult', 'Ogre', 'Omen', 'Oppressor', 'Fear']
    negativeAdjectives = ['Misty', 'Moaning', 'Mourning', 'Mysterious', 'Mystic', 'Mythical']
    positiveNames = ['Cloud', 'Sky', 'Moonshine', 'Moonlight', 'Moonbeam', 'Moonstone', 'Morningstar', 'Myth', 'Noon']
    treeNames = ['Oak', 'Beech', 'Birch', 'Alder', 'Spurce', 'Maple', 'Larch', 'Fir', 'Plane', 'Elm']
    streamNames = ['Stream', 'Brook', 'Creek', 'Beck', 'Rivulet', 'Ditch', 'Runnel', 'Burn']
    flowerNames = ['Rose', 'Tulip', 'Orchid']
    treePartNames = ['Thorn', 'Blossom', 'Branch', 'Limb', 'Knag', 'Leaf']
    plantNames = ['Mulberry', 'Myrrh', 'Myrtle', 'Hawthorn', 'Blackthorn', 'Blackberry', 'Bramble', 'Nettle']
    thingNames = ['Moleskin', 'Mushroom']
    birdNamesFirstPart = ['Raven', 'Eagle', 'Buzzard', 'Hawk', 'Owl', 'Falcon', 'Blackbird']
    birdNamesSecondPart = ['eye', 'claw', 'beak', 'wings', 'feather']
    # The element names are defined by a tuple. elements that have no plural are False
    elementNames = [('Silver', False), ('Emerald', True), ('Ruby', True), ('Crystal', False), ('Pearl', True), ('Jasmin', True), \
                    ('Diamond', True), ('Onyx', False), ('Opal', True), ('Rose', True), ('Pearl', True), ('Iron', False), ('Steel', False), \
                    ('Obsidian', True), ('Sapphire', True), ('Jade', False), ('Glimmer', False), ('Bronce', False), ('Gold', False), ('Glass', False), \
                    ('Amber', False), ('Platinum', 'False'), ('Coal', False)]

if __name__ == '__main__':
    unittest.main()
