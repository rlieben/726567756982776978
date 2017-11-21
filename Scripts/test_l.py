# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Test script for Luc.
'''



'''
First algorithm that places one house, used to test the classes of classes.py.
'''

from classes import *
from functions import *
from visuals import *

ah_map = random_generator()

freespace = calc_freespace(ah_map.houses[4], ah_map)

# scatterplot(ah_map)
