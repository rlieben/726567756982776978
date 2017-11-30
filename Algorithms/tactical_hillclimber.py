
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
import copy

# input is empty map, output is value calculated
def tactical_hillclimber(map_charac, tries_random, tries_hill, nr_houses):
	'''Moves houses on map based on highest freespace.

	Input arguments:
	map_charac -- map characteristics
	tries_random -- number of random maps created
	tries_hill -- number of hillclimbing
	nr_houses -- nr of houses that are moved with each hillclimb
	'''

	best_map = best_of_random(MAP_20, tries_random)
	maximum = best_map.calc_score()

	for i in range(tries_hill):
		try_map = copy.copy(best_map)
		try_map.tactical_swap_houses(nr_houses)

		print(i)

		score = try_map.calc_score()

		if score > maximum:
			maximum = score
			best_map = try_map

	return best_map
