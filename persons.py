#!/usr/bin/env python.

"""

  This is the persons module of the Duke of Silvershire
  
"""

import random
import unittest
from standardNames import StandardNames
from person import Person
from races import Race

__author__ = "Sven Eggert"
__copyright__ = "Copyright 2017, Egertiko Designs"
__credits__ = []

__license__ = "GPL"
__version__ = "0.0.9"
__maintainer__ = "Sven Eggert"
__email__ = "sven674@web.de"
__status__ = "Development"

"""
  The Person is an individual in the Duke of Silvershire and has a name
"""
class Persons(unittest.TestCase):
  titleNames = ['Lord', 'Bishop', 'Wizard', 'Sorcerer', 'Duke', 'Earl', 'Barron', 'Grand Duke', 'King' , 'Sir', 'Prince', 'Principality', 'Chancellor', 'Monarch', \
                'Abbot', 'Aldermen', 'Archduke', 'Archbishop']
  additionalEvilTitleNames = ['Dead', 'Black']
  MIN_RIDERS = 100
  MAX_RIDERS = 500
  MIN_WARRIORS = 500
  MAX_WARRIORS = 5000

  """
    Create a name by an element and a birds name
  """
  def _createPersonNameByElementBird(self):
    titleName = random.choice(StandardNames.elementNames)[0]
    birdName = random.choice(StandardNames.birdNamesFirstPart)
    titleName += "-" + birdName.title()

    return titleName

  """
    Create a name by an birds name
  """


  def _createPersonNameByBird(self):
    titleName = random.choice(StandardNames.birdNamesFirstPart)
    birdName = random.choice(StandardNames.birdNamesSecondPart)
    titleName += "-" + birdName.title()

    return titleName

  """
    Create one person
  """
  def createPerson(self, race, loyality):
    person = Person()
    person.race = race

    if race == Race.DEADLORD:
      person.is_evil = True
      person.loyality = 0.0
    else:
      person.loyality = loyality
      
    if race in [Race.HUMAN, Race.DEADLORD]:
      person.riders = random.randrange(self.MIN_RIDERS, self.MAX_RIDERS, 100)
      person.warriors = random.randrange(self.MIN_WARRIORS, self.MAX_WARRIORS, 500)
    else:
       person.riders = -1 # cannot have any riders
       person.warriors = random.randrange(self.MIN_WARRIORS, self.MAX_WARRIORS, 500)

    person.name = self.createPersonName (person.is_evil)

    return person
      
  """
    Main routine to create all persons. In this case all
    positive persons

    quantity      True if the person is a dead lord
  """
  def createPersons(self, quantity):   
    x = quantity
    while x > 0:
      person = self.createPersonName (False)
      
      x = x - 1  

  """
    Main routine to create a persons name

    deadLord      True if the person is a dead lord
  """
  def createPersonName(self, deadLord):
    titleName = random.choice(self.titleNames)

    if deadLord:
      titleName = random.choice(self.additionalEvilTitleNames) + " " + titleName

      whatName = random.random()
      
      if whatName < 0.7:
        titleName += " of "
        titleName += random.choice(StandardNames.negativeNames)
      else:
        titleName += " the "
        titleName += random.choice(StandardNames.specialNegativeNames)
    else:
      whatName = random.randint(1,3)
      if whatName == 1:
        titleName += " " + self._createPersonNameByBird()
      elif whatName == 2:
        titleName += " the " + random.choice(StandardNames.specialPositiveNames)
      else:
        titleName += " " + self._createPersonNameByElementBird()  

    return titleName
    
  """
    Test creating persons
  """
  def test_createPersons(self):
    x = 100
    while x > 0:
      race = random.randint(Race.FIRST_RACE, Race.LAST_RACE)
      if race == Race.DEADLORD:
        loyality = 0.0
      else:
        loyality = random.random()
  
      person = self.createPerson (race, loyality)
      print (person.name, person.race, person.loyality, person.riders, person.warriors, person.loyality)  
      
      x = x - 1  

if __name__ == '__main__':
    unittest.main()
