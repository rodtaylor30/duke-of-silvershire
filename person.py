#!/usr/bin/env python.

"""

  This is the person module of the Duke of Silvershire
  
"""

import random
import unittest
from standardNames import StandardNames
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
class Person(unittest.TestCase):
  """
    Name of the person
  """
  name = ""

  """
    Is the person a bad peraon or if not good
  """
  is_evil = False

  """
    What is the loyality of the person
    1.0 loyal
    0.0 unloyal
  """
  loyality = False

  """
    The location of the person
  """
  location = (0,0)

  """
    How many riders has the person
  """
  riders = 0

  """
    How many warriors has the person
  """
  warriors = 0

  """
    How much is the strength of the person
    
    example: 1.0 means very good, 0.0 is low
  """
  strength = 1.0

  """
    How much is the strength of his army
    
    example: 1.0 means very good, 0.0 is low
  """
  strength_warrios = 1.0

  """
    How much is the strength of his army
    
    example: 1.0 means very good, 0.0 is low
  """
  strength_riders = 1.0

  """
    The race of the person
  """
  race = Race.HUMAN
  
if __name__ == '__main__':
    unittest.main()

