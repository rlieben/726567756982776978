# Group:        726567756982776978
# Assignment:   Amstelhaege

'''
First algorithm that places houses, used to test the classes of classes.py.
'''

from classes import *

def create_test():
    ah_map = Map(WIDTH_MAP, HEIGHT_MAP)

    for y in range(HEIGHT_MAP):
        for x in range(WIDTH_MAP):


    # tries to place one house
    ah_map.houses.append(One_Family(0))

    for i in range(x_loc, x_loc + SIZE_1F[0]):
        for j in range(y_loc, y_loc + SIZE_1F[1]):
            ah_map.houses[0].add_structure(i, j)

    for cell in ah_map.houses[0].structure:
        ah_map.grid[cell[0]][cell[1]].type = 'house'

    return ah_map