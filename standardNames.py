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
                     'Obscurity', 'Obstacles', 'Occult', 'Ogre', 'Omen', 'Oppressor', 'Fear', 'Abandonment', 'Abasement', 'Abashment', 'Abattoir', 'Abeyance', \
                     'Abhorrence', 'Abjection', 'Abomonation', 'Abyss', 'Acrimony', 'Adjuration', 'Adversity', 'Affliction', 'Aggression', 'Agony', \
                     'Animosity', 'Annihilation', 'Annoyance', 'Anxiety', 'Apostasy', 'Archfiend', 'Atrocity', 'Audacity', 'Avidity', 'Aversion', \
                     'Baal', 'Babylon', 'Badness', 'Banishment', 'Banshee', 'Barrenness', 'Barrow', 'Bestiality']
    negativeAdjectives = ['Misty', 'Moaning', 'Mourning', 'Mysterious', 'Mystic', 'Mythical', 'Ablaze', 'Abstruse', 'Acid', 'Afire', 'Aflame']
    positiveAdjectives = ['Adamantine', 'Adventurous']
    positiveNames = ['Cloud', 'Sky', 'Moonshine', 'Moonlight', 'Moonbeam', 'Moonstone', 'Morningstar', 'Myth', 'Noon', 'Acquiescence', 'Acumen', 'Adequancy', \
                     'Adventure', 'Aeon', 'Aerie', 'Affability', 'Affiance', 'Afterglow', 'Age', 'Agility', 'Autumn']
    specialPositiveNames = ['Anvil', 'Hammer', 'Axe', 'Armourer', 'Arrow', 'Arrowhead']
    specialNegativeNames = ['Abettor', 'Aggressor', 'Agitator', 'Assasin', 'Attacker', 'Autocrat', 'Barbarian', 'Besieger', 'Betrayer']
    herbsNames = ['Acanthus', 'Aconite', 'Arrowroot', 'Bard']
    streamNames = ['Stream', 'Brook', 'Creek', 'Beck', 'Rivulet', 'Ditch', 'Runnel', 'Burn']
    flowerNames = ['Rose', 'Tulip', 'Orchid', 'Aster']
    treeNames = ['Oak', 'Beech', 'Birch', 'Alder', 'Spurce', 'Maple', 'Larch', 'Fir', 'Plane', 'Elm', 'Acacia', 'Acorn', 'Ash', 'Asp', 'Aspen']
    treePartNames = ['Thorn', 'Blossom', 'Branch', 'Limb', 'Knag', 'Leaf', 'Bark']
    plantNames = ['Mulberry', 'Myrrh', 'Myrtle', 'Hawthorn', 'Blackthorn', 'Blackberry', 'Bramble', 'Nettle', 'Agave']
    thingNames = ['Moleskin', 'Mushroom']
    negativeAnimals = ['Adder']
    positiveAnimals = ['Badger']
    birdNamesFirstPart = ['Raven', 'Eagle', 'Buzzard', 'Hawk', 'Owl', 'Falcon', 'Blackbird']
    birdNamesSecondPart = ['eye', 'claw', 'beak', 'wings', 'feather']
    # The element names are defined by a tuple. Elements that have no plural are False
    elementNames = [('Silver', False), ('Emerald', True), ('Ruby', True), ('Crystal', False), ('Pearl', True), ('Jasmin', True), \
                    ('Diamond', True), ('Onyx', False), ('Opal', True), ('Rose', True), ('Pearl', True), ('Iron', False), ('Steel', False), \
                    ('Obsidian', True), ('Sapphire', True), ('Jade', False), ('Glimmer', False), ('Bronce', False), ('Gold', False), ('Glass', False), \
                    ('Amber', False), ('Platinum', 'False'), ('Coal', False), ('Agate', True), ('Alabaster', False), ('Amethyst', True), \
                    ('Basalt', False), ('Beryl', True)]
    chemicalsNames = ['Alum', 'Ammonia', 'Argil', 'Arsenic']
    adjectiveNamesMen = ['Strong', 'Curage', 'Sturdy']
    partsMen = ['fist', 'foot', 'arm', 'neck', 'eye', 'back']
    colorNames = ['Azure']

if __name__ == '__main__':
    unittest.main()
