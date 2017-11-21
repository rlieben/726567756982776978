# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

from classes import *
import numpy

'''
All basic functions to operate on the map.
'''

def place_house(ah_map, loc, house_id, type_charac):
    '''Places a one family house on location on the map, with a given id.'''

    # adds class to list of houses in the map
    ah_map.houses.append(House(house_id, type_charac, loc))

    return ah_map



def calc_freespace(newhouse, ah_map):

	# coordinates new house
	x_newhouse = newhouse.loc['x']
	y_newhouse = newhouse.loc['y']

	# set freespace variable
	freespace = 0

	# iterate over all houses in map
	for house in ah_map.houses:

		# calculate x and y difference new and curr
		diff_housescurr[0] = ah_map.houses[house].loc['x'] - x_newhouse
		diff_housescurr[1] = ah_map.houses[house].loc['y'] - y_newhouse

		# calculate x and y difference new and next
		diff_housesnext[0] = ah_map.houses[house + 1].loc['x'] - x_newhouse
		diff_housesnext[1] = ah_map.houses[house + 1].loc['y'] - y_newhouse

		# calculates distance between new and current
		distancecurr = sqrt((diff_housescurr[0] ^ 2) + (diff_housescurr[1] ^ 2))
		distancenext = sqrt((diff_housesnext[0] ^ 2) + (diff_housesnext[1] ^ 2))

		# update if distance from current is greater than next
		if distancecurr < distancenext:

			freespace = distancecurr

		else:

			freespace = distancenext

	print (freespace)
	return freespace


data = create_test()

print (data.houses)
