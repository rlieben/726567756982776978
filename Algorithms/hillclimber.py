
import sys
list_dir = sys.path[0].split('\\')
string = ''
for i in range(len(list_dir) - 1):
    string += list_dir[i]
    string += '\\'

sys.path.insert(0, string)

from Classes.house_class import *
from Classes.map_class import *
from Classes.water_class import *
from Types.Characteristics_Amstelhaege import *
from Algorithms.best_of_random import *
import random
import numpy

# input is empty map, output is value calculated
def hillclimber(map_charac, tries_random, tries_hill, nr_houses):
	'''Moves, every iteration, three houses for optimalization.

	Input arguments:
	map_charac -- map characteristics
	tries_random -- number of random maps created
	tries_hill -- number of hillclimbing
	nr_houses -- nr of houses that are moved with each hillclimb
	'''

	best_map = best_of_random(MAP_20, tries_random)
	maximum = best_map.score

	for i in range(tries_hill):
		ah_map = random_swap_houses(best_map, nr_houses)
		summy = 0
		for house in ah_map.houses:
			house.calc_freespace(ah_map)
			house.calc_value()
			summy += house.value

		if summy > maximum:
			maximum = summy
			best_map = ah_map

	best_map.score = maximum
	return best_map
