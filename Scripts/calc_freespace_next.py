import os
from classes import *
from premises import *
import math

def calc_freespace(newhouse):

	# coordinates new house
	x_newhouse = newhouse.loc['x']
	y_newhouse = newhouse.loc['y']

	# # difference between center and wall of house
	# x_diffhouse = newhouse.charac['width'] / 2
	# y_diffhouse = newhouse.charac['height'] / 2

	# # bounds coordinates new house
	# x_lowerbound = x_newhouse - x_diffhouse
	# x_upperbound = x_newhouse + x_diffhouse
	# y_lowerbound = y_newhouse - y_diffhouse
	# y_upperbound = y_newhouse + y_diffhouse

	


	# # iterate over all houses in map
	# for house in Map.houses:

	# 	# absolute difference between new and existing house
		# diff_houses[0] = sqrt((Map.houses[house].loc['x'] - x_newhouse) ^ 2))
		# diff_houses[1] = sqrt((Map.houses[house].loc['y'] - y_newhouse) ^ 2))

	# 	# check if not a corner wall
	# 	if Map.houses[house].loc['x'] > x_lowerbound and Map.houses[house].loc['x'] < x_upperbound:

	# 		# check if smaller than next element
	# 		if diff_houses[0] < Map.houses[house + 1].loc['x'] - x_newhouse:

	# 			# check if y is also smaller
	# 			if diff_houses[1] < Map.houses[house + 1].loc['y'] - x_newhouse:

	freespace = 0
	# iterate over all houses in map
	for house in Map.houses:

		# calculate x and y difference new and curr
		diff_housescurr[0] = Map.houses[house].loc['x'] - x_newhouse
		diff_housescurr[1] = Map.houses[house].loc['y'] - y_newhouse

		# calculate x and y difference new and next
		diff_housesnext[0] = Map.houses[house + 1].loc['x'] - x_newhouse
		diff_housesnext[1] = Map.houses[house + 1].loc['y'] - y_newhouse

		# calculates distance between new and current
		distancecurr = sqrt((diff_housescurr[0] ^ 2) + (diff_housescurr[1] ^ 2))
		distancenext = sqrt((diff_housesnext[0] ^ 2) + (diff_housesnext[1] ^ 2))

		# update if distance from current is greater than next
		if distancecurr < distancenext:

			freespace = distancecurr

		else:

			freespace = distancenext

	return freespace