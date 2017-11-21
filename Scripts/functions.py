# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

import os
from classes import *
from case import *
import numpy

'''
All basic functions to operate on the map.
'''

def place_house(ah_map, loc, house_id, type_charac):
    '''Places a one family house on location on the map, with a given id.'''

    new_house = House(house_id, type_charac, loc)

    if house_id == 0:
        ah_map.houses.append(new_house)
    else:
        ah_map.calc_freespace(new_house)

        if new_house.freespace < new_house.charac['min_free']:
            return False
        else:
            ah_map.houses.append(new_house)
        # return ah_map
