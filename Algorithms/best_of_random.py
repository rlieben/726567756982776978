# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


def best_of_random(map_specs, tries, save_steps=False):
	''' Creates random maps and returns the map with the highest score.

	Input arguments:
	map_specs -- type specifications of the case, from file in folder specifications
	tries -- integer, number of random maps created
	save_steps -- boolean, saving each step/map for visualization

	Example: best_of_random(MAP_20, 3, True)
	'''

	from __import__ import random_generator, split, coloured_map

	k = 0
	maximum = 0
	best_map = random_generator(map_specs)
	data = []
	steps = []

	for i in range(tries):
		try_map = random_generator(map_specs)

		if save_steps == True:
			coloured_map(try_map, 'best_of_random60' + split + 'tmp_gif',
						 (str(k).zfill(3)))
			k += 1
			steps.append(try_map)

		score = try_map.calc_score()

		data.append(score)

		if score > maximum:
			maximum = score
			best_map = try_map

	return {'best_map' : best_map, 'data' : data, 'steps' : steps}


if __name__ == '__main__':

	from __import__ import MAP_60, coloured_map, save_results, make_gif, plot_data

	best_random_map = best_of_random(MAP_60, 10, True)
	# test_random = best_of_random(MAP_20, 10, False)

	coloured_map(best_random_map['best_map'], 'best_of_random60', 'best')
	plot_data([best_random_map['data']], 'best_of_random60', 'plot')
	save_results(best_random_map['data'], 'best_of_random60', 'data')
	make_gif(best_random_map['steps'], 'best_of_random60', 'random')
