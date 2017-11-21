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

    ah_map.houses.append(House(house_id, type_charac, loc))

    return ah_map


def calc_freespace(newhouse, ah_map):

    # coordinates new house
    x_newhouse = newhouse.location['x']
    y_newhouse = newhouse.location['y']

    diff_housescurr = [0, 0]

    # calculate x and y difference new and first and calc freespace variable
    diff_housescurr[0] = ah_map.houses[0].location['x'] - x_newhouse
    diff_housescurr[1] = ah_map.houses[0].location['y'] - y_newhouse
    freespace = numpy.sqrt(numpy.power(diff_housescurr[0], 2) + numpy.power(diff_housescurr[1], 2))

    # iterate over all houses in map
    for house in ah_map.houses:

        if house.self_id != newhouse.self_id:
            # calculate x and y difference new and curr
            diff_housescurr[0] = house.location['x'] - x_newhouse
            diff_housescurr[1] = house.location['y'] - y_newhouse

            # print("housediff")
            # print(diff_housescurr)

            # calculates distance between new and current
            distancecurr = numpy.sqrt(numpy.power(diff_housescurr[0], 2) + numpy.power(diff_housescurr[1], 2))

            # update if freespace is greater than curr distance
            if freespace >= distancecurr:

            	freespace = distancecurr

    print (freespace)
    return freespace
