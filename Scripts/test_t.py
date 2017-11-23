# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Test script for Toon.
'''

from classes import *
from functions import *
from algorithms import *
from visuals import *


'''
Test script for Luc.
'''

from classes import *
from functions import *
from visuals import *
from algorithms import *


# print(ah_map.houses[0].corners)
ah_map = Map(MAP['width'], MAP['height'])

maximum = 0
best_map = random_generator()

for i in range(100):
    hill_climber(ah_map)

scatterplot(best_map)
