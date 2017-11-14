# Group:        726567756982776978
# Assignment:   Amstelhaege

from classes import *

'''
All basic functions to operate on the map.
'''

def place_one_family(ah_map, loc, house_id):
    '''Places a one family house on location on the map, with a given id.'''

    # adds class to list of houses in the map
    ah_map.houses.append(One_Family(house_id))

    # starting from the corner with lowest x and y value, iterates over width
    # and height of the house to add coordinates to list of the class
    for i in range(loc['x'], loc['x'] + SIZE_1F[0]):

        for j in range(loc['y'], loc['y'] + SIZE_1F[1]):

            ah_map.houses[len(ah_map.houses) - 1].add_structure({'x' : i,
                                                                 'y' : j})


    # checks if house can be placed
    for cell in ah_map.houses[len(ah_map.houses) - 1].structure:

        if ah_map.grid[cell['x']][cell['y']].type != 'empty':
            return False


    # changes the type in the grid of the map
    for cell in ah_map.houses[len(ah_map.houses) - 1].structure:

        ah_map.grid[cell['x']][cell['y']].type = 'one_family'

    return ah_map


def place_bungalow(ah_map, loc, house_id):
    '''Places a bungalow on location on the map, with a given id.'''

    # adds class to list of houses in the map
    ah_map.houses.append(Bungalow(house_id))

    # starting from the corner with lowest x and y value, iterates over width
    # and height of the house to add coordinates to list of the class
    for i in range(loc['x'], loc['x'] + SIZE_BU[0]):

        for j in range(loc['y'], loc['y'] + SIZE_BU[1]):

            ah_map.houses[len(ah_map.houses) - 1].add_structure({'x' : i,
                                                                 'y' : j})

    # checks if house can be placed
    for cell in ah_map.houses[len(ah_map.houses) - 1].structure:

        if ah_map.grid[cell['x']][cell['y']].type != 'empty':
            return False


    # changes the type in the grid of the map
    for cell in ah_map.houses[len(ah_map.houses) - 1].structure:

        ah_map.grid[cell['x']][cell['y']].type = 'bungalow'

    return ah_map


def place_mansion(ah_map, loc, house_id):
    '''Places a mansion on location on the map, with a given id.'''

    # adds class to list of houses in the map
    ah_map.houses.append(Mansion(house_id))

    # starting from the corner with lowest x and y value, iterates over width
    # and height of the house to add coordinates to list of the class
    for i in range(loc['x'], loc['x'] + SIZE_MA[0]):

        for j in range(loc['y'], loc['y'] + SIZE_MA[1]):

            ah_map.houses[len(ah_map.houses) - 1].add_structure({'x' : i,
                                                                 'y' : j})

    # checks if house can be placed
    for cell in ah_map.houses[len(ah_map.houses) - 1].structure:

        if ah_map.grid[cell['x']][cell['y']].type != 'empty':
            return False


    # changes the type in the grid of the map
    for cell in ah_map.houses[len(ah_map.houses) - 1].structure:

        ah_map.grid[cell['x']][cell['y']].type = 'mansion'

    return ah_map
