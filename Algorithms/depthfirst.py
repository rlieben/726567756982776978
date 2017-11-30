import sys
list_dir = sys.path[0].split('\\')
string = ''
for i in range(len(list_dir) - 1):
	string += list_dir[i]
	string += '\\'

sys.path.insert(0, string)

from Classes.house import *
from Classes.map import *
from Classes.water import *
from Characteristics.Amstelhaege import *
from Algorithms.best_of_random import *
from Algorithms.helpers import *
import random
import numpy

def depthfirst(ah_map, runs):
	''' Places house random and searches for the best child. 

	Input arguments:
	ah_map -- empty map
	runs -- integer, how many runs of the function

	Returns:
	ah_map -- best map with 20 houses
	score -- score of best map
	'''

	# initializes map
	ah_map = Map(MAP_20)

	# initialize score variables
	tmpscore = 0
	score = 0

	# amount of runs for script
	for run in range(runs):

		# iterates over perc houses
		for j in range(ah_map.distr_houses):

			# iterates over type houses
			for i in range(ah_map.distr_houses[j] * ah_map.nr_houses):

				# sets house id
				house_id = 100 * (j + 1) + i

				# gets location where the most freespace is
				loc = ah_map.calc_freespace_on_map(House(house_id, ah_map.types[j], {'x' : None, 'y' : None))

				# places house on location with most freespace
				ah_map.place_house(loc, house_id, ah_map.types[j])

		# calc score of created map
		tmpscore = ah_map.calc_score()

		# update best score if greater
		if tmpscore > score:

		score = tmpscore

	# returns created map and score
	return ah_map
	return score


