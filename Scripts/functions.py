# Group:        726567756982776978
# Assignment:   Amstelhaege

from classes.py import *


def place_one_family(ah_map, loc, house_id):
    ah_map.houses.append(One_Family(house_id))

    for i in range(loc['x'], loc['x'] + SIZE_1F[0]):
        for j in range(loc['y'], loc['y'] + SIZE_1F[1]):
            ah_map.houses[len(ah_map.houses)].add_structure(i, j)

    for cell in ah_map.houses[len(ah_map.houses)].structure:
        ah_map.grid[cell['x']][cell['y']].type = 'one_family'

    return ah_map


def place_bungalow(ah_map, loc, house_id):
    ah_map.houses.append(Bungalow(house_id))

    for i in range(loc['x'], loc['x'] + SIZE_BU[0]):
        for j in range(loc['y'], loc['y'] + SIZE_BU[1]):
            ah_map.houses[len(ah_map.houses)].add_structure(i, j)

    for cell in ah_map.houses[len(ah_map.houses)].structure:
        ah_map.grid[cell['x']][cell['y']].type = 'bungalow'

    return ah_map


def place_mansion(ah_map, loc, house_id):
    ah_map.houses.append(Mansion(house_id))

    for i in range(loc['x'], loc['x'] + SIZE_MA[0]):
        for j in range(loc['y'], loc['y'] + SIZE_MA[1]):
            ah_map.houses[len(ah_map.houses)].add_structure(i, j)

    for cell in ah_map.houses[len(ah_map.houses)].structure:
        ah_map.grid[cell['x']][cell['y']].type = 'mansion'

    return ah_map
