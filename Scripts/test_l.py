# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Test script for Luc.
'''

from classes import *
from functions import *
from visuals import *
from algorithms import *

ah_map = random_generator()

# print(ah_map.houses[0].corners)

freespace = calc_freespaceforreal(ah_map.houses[4], ah_map)

print(freespace)

# scatterplot(ah_map)
