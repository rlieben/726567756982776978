
from __import__ import *

def best_of_random(map_charac, tries):
	''' Creates random maps and returns the map with the highest score.

	Input arguments:
	map_charac -- characteristics of the map
	tries -- number of creating random maps
	'''

	maximum = 0
	best_map = random_generator(map_charac)

	for i in range(tries):
		try_map = random_generator(map_charac)

		score = try_map.calc_score()

		if score > maximum:
			maximum = score
			best_map = try_map

	return best_map