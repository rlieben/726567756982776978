# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Test script for Toon.
'''

'''
First algorithm that places one house, used to test the classes of classes.py.
'''

from classes import *
from functions import *
from visuals import *

ah_map = Map(WIDTH_MAP, HEIGHT_MAP)

x_loc = 5
y_loc = 5

# tries to place one house
ah_map.houses.append(One_Family(0))

def create_test():
    ah_map = Map(WIDTH_MAP, HEIGHT_MAP)

    loc = {'x' : 5, 'y' : 5}

    place_one_family(ah_map, loc, 0)

    scatterplot(ah_map)

    # # tries to place one house
    # ah_map.houses.append(One_Family(0))
    #
    # for i in range(x_loc, x_loc + SIZE_1F[0]):
    #     for j in range(y_loc, y_loc + SIZE_1F[1]):
    #         ah_map.houses[0].add_structure(i, j)
    #
    # for cell in ah_map.houses[0].structure:
    #     ah_map.grid[cell[0]][cell[1]].type = 'house'

    return ah_map
