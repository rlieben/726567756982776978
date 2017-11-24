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

        if new_house.freespace < MANSION['min_free']:
            return False
        else:
            ah_map.houses.append(new_house)
        # return ah_map

def calc_freespace_on_map(ah_map, new_house):
    '''Calculating most freespace on map and receives map and movable house as input'''

    # initiate possible freespace variable
    poss_freespace = 0

    # initiate x and y variable for optimization
    best_x = new_house.location['x']
    best_y =  new_house.location['y']

    # iterate over map width
    for i in range(len(ah_map.charac['width'])):

        # iterate over map height
        for j in range(len(ah_map.charac['height'])):

            # set x and y location of new house
            new_house.location['x'] = i
            new_house.location['y'] = j

            # store the possible freespace of new location
            tmp = ah_map.calc_freespace(new_house)

            # if new freespace is greater then update
            if (tmp > poss_freespace):

                # update new poss freespace
                poss_freespace = tmp

                # update location of poss freespace
                best_x = i
                best_y = j

            # increment j to skip through map
            j += 5

        # increment i to skip through map
        i += 5




