
from __import__ import *

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

	print (maximum)
	print("test")
	print(tries_hill)

	for i in range(tries_hill):
		try_map = copy.copy(best_map)
		score_trymap = try_map.calc_score()
		print("1")
		print (score_trymap)
		try_map.tactical_swap_houses(nr_houses)

		print("2")
		print(try_map.calc_score())

		print("test2")
		print(i)

		score = try_map.calc_score()



		if score > maximum:
			maximum = score
			best_map = try_map

	return best_map
