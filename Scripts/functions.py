# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

from classes import *

'''
All basic functions to operate on the map.
'''

def place_house(ah_map, loc, house_id, type_charac):
    '''Places a one family house on location on the map, with a given id.'''

    # adds class to list of houses in the map
    ah_map.houses.append(House(house_id, type_charac))

    # put location in list of houses in local variable
    nr = len(ah_map.houses) - 1

    # starting from the corner with lowest x and y value, iterates over width
    # and height of the house to add coordinates to list of the class
    for i in range(loc['x'], loc['x'] + ah_map.houses[nr].charac['width']):

        for j in range(loc['y'], loc['y'] + ah_map.houses[nr].charac['height']):

            ah_map.houses[nr].add_structure({'x' : i, 'y' : j})

    # checks if house can be placed
    for cell in ah_map.houses[nr].structure:

        if ah_map.grid[cell['x']][cell['y']].type != 'empty':
            return False


    # changes the type in the grid of the map
    for cell in ah_map.houses[nr].structure:

        ah_map.grid[cell['x']][cell['y']].type = ah_map.houses[nr].charac['type']

    return ah_map



def calc_freespace(ah_map, loc):
        '''Calculates freespace of house, with top-left coordinates of
           structure.'''

        # # initialize freespace coordinates
        # freespace_x = 0
        # freespace_y = 0


        # for i in range(length house):


        #         # iterates over xaxis
        #         for x in range(ah_map.measures['width']):

        #             # iterates over yaxis
        #             for y in range(ah_map.measures['height']):


        #                 # runs untill cell is other type than empty
        #                 if ah_map.grid[x][y].type != 'empty':
