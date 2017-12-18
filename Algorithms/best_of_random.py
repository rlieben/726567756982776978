# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import copy


def best_of_random(map_specs, tries, save_steps=False):
	''' Creates random maps and returns the map with the highest score.

	Input arguments:
	map_specs -- dict, map specifications from file in folder Specifications
	tries -- integer, number of random maps created
	save_steps -- boolean, saving each step/map for visualization

	Example: best_of_random(MAP_20, 3, True)
	'''

	from __import__ import random_generator

	# intialize variable
	maximum = 0

	# intialize random map, which is best map so far
	best_map = random_generator(map_specs)

	# initializes empty list for data and maps
	data = []
	steps = []

	# iterate over tries
	for i in range(tries):

		# generate random map
		try_map = random_generator(map_specs)

		# append map for visualization
		if save_steps == True:
			steps.append(copy.deepcopy(try_map))

		# calculate and append score
		score = try_map.calc_score()
		data.append(score)

		# update best map if score is greater
		if score > maximum:
			maximum = score
			best_map = try_map

	return {'best_map' : best_map, 'data' : data, 'steps' : steps}


if __name__ == '__main__':

	from __import__ import MAP_60, coloured_map, save_results, make_gif, \
						   plot_data, MAP_20

	best_random_map = best_of_random(MAP_20, 10, False)

	# coloured_map(best_random_map['best_map'], 'best_of_random', 'best')
	# plot_data([best_random_map['data']], 'best_of_random', 'plot')
	# save_results(best_random_map['data'], 'best_of_random', 'data')
	# make_gif(best_random_map['steps'], 'best_of_random', 'random')
