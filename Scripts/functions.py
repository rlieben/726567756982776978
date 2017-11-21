# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

import os
from classes import *
from case import *
import math
# from algorithms import *

'''
All basic functions to operate on the map.
'''

def place_house(ah_map, loc, house_id, type_charac):
    '''Places a one family house on location on the map, with a given id.'''

    # adds class to list of houses in the map
    # for i in range(house_id - 1):
    #     free_space = loc['x'][i] - loc['x'][i + 1]
    #     if free_space > ONE_FAM['min_free']
    ah_map.houses.append(House(house_id, type_charac, loc))

    return ah_map


def calc_freespace(newhouse, ah_map):

	# coordinates new house
	x_newhouse = newhouse.loc['x']
	y_newhouse = newhouse.loc['y']

	# calculate x and y difference new and curr and calc freespace variable
	diff_housescurr[0] = ah_map.houses[house].loc['x'] - x_newhouse
	diff_housescurr[1] = ah_map.houses[house].loc['y'] - y_newhouse
	freespace = sqrt((diff_housescurr[0] ^ 2) + (diff_housescurr[1] ^ 2))

	# iterate over all houses in map
	for house in ah_map.houses:

		# calculate x and y difference new and curr
		diff_housescurr[0] = ah_map.houses[house].loc['x'] - x_newhouse
		diff_housescurr[1] = ah_map.houses[house].loc['y'] - y_newhouse

		# calculates distance between new and current
		distancecurr = sqrt((diff_housescurr[0] ^ 2) + (diff_housescurr[1] ^ 2))

		# update if freespace is greater than curr distance
		if freespace >= distancecurr:

			freespace = distancecurr

	print (freespace)
	return freespace
