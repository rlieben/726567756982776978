# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import copy


def hillclimber(map_specs, tries_random, tries_hill, nr_houses, hill_type,
				save_steps = False):
	'''Moves, every iteration, houses for optimalization.

	Input arguments:
	map_specs -- type specifications of the case, from file in folder specifications
	tries_random -- integer, number of random maps created
	tries_hill -- integer, number times of hillclimbing
	hill_type -- integer, type of hillclimber(0: random, 1:tactical, based on most freespace)
	save_steps -- boolean, saving each step/map for visualization

	Returns dictionary containing:
	best_map -- object, best map
	data -- list, scores of maps
	steps -- list, with all created maps

	Example: hillclimber(MAP_20, 40, 5, 1, True)
	'''

	from __import__ import split, coloured_map, best_of_random

	best_map = best_of_random(map_specs, tries_random)['best_map']
	maximum = best_map.calc_score()

	data = []
	steps = []
	k = 0

	for i in range(tries_hill):

		try_map = copy.copy(best_map)

		if (hill_type == 0):

			try_map.random_swap_houses(nr_houses)
			folder = 'hillclimber'

		elif (hill_type == 1):

			try_map.tactical_swap_houses(nr_houses)
			folder = 'tactical_hillclimber'

		score = try_map.calc_score()

		if score > maximum:
			maximum = score
			best_map = try_map

		data.append(maximum)

		if save_steps == True:
			coloured_map(best_map, folder + split + 'tmp_gif',
						 str(k).zfill(3))
			k += 1
			steps.append(best_map)

	return {'best_map' : best_map, 'data' : data, 'steps' : steps}


if __name__ == '__main__':

	from __import__ import MAP_60, coloured_map, save_results, make_gif, \
						   best_of_random, plot_data

	hillclimber_map = hillclimber(MAP_60, 1, 10, 1, 0, True)
	# tactical_hillclimber_map = hillclimber(MAP_20, 1, 10, 1, 1, True)

	plot_data(hillclimber_map['data'], 'hillclimber60', 'plot')
	coloured_map(hillclimber_map['best_map'], 'hillclimber60', 'best')
	save_results(hillclimber_map['data'], 'hillclimber60', 'data')
	make_gif(hillclimber_map['steps'], 'hillclimber60', 'hillclimber')

	# plot_data(tactical_hillclimber_map['data'], 'tactical_hillclimber', 'plot')
	# coloured_map(hillclimber_map['best_map'], 'tactical_hillclimber', 'best')
	# save_results(hillclimber_map['data'], 'tactical_hillclimber', 'data')
	# make_gif(hillclimber_map['steps'], 'tactical_hillclimber', 'tactical_hillclimber')
