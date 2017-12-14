
from __import__ import *

def best_of_random(map_charac, tries, save_steps=False):
	''' Creates random maps and returns the map with the highest score.

	Input arguments:
	map_charac -- characteristics of the map
	tries -- number of creating random maps
	'''

	maximum = 0
	best_map = random_generator(map_charac)
	data = []
	steps = []

	for i in range(tries):
		try_map = random_generator(map_charac)

		if save_steps == True:
			steps.append(try_map)

		score = try_map.calc_score()

		data.append(score)

		if score > maximum:
			maximum = score
			best_map = try_map

	return {'best_map' : best_map, 'data' : data, 'steps' : steps}


if __name__ == '__main__':

	from __import__ import *

	best_random_map = best_of_random(MAP_20, 20, True)

	coloured_map(best_random_map['best_map'], 'best_of_random', 'best')
	save_results(best_random_map['data'], 'best_of_random', 'data')
	make_gif(best_random_map['steps'], 'best_of_random', 'random')
