# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import copy


def hillclimber(in_map, tries_hill, nr_houses, hill_type, save_steps = False):

	'''Moves a number of houses per iteration on either a random place, or on
	   the place with the most freespace.

	Input arguments:
	in_map -- object, map to hillclimb
	tries_hill -- integer, number times of hillclimbing
	nr_houses -- integer, number of houses to swap
	hill_type -- integer, type of hillclimber (0 : random,
											   1 : based on most freespace)
	save_steps -- boolean, saving each step/map for visualization

	Returns dictionary containing:
	best_map -- object, best map
	data -- list of floats, scores of maps
	steps -- list of objects, all created maps

	Example: hillclimber(MAP_20, 40, 5, 1, True)
	'''

	# copy input map as current best map
	best_map = copy.deepcopy(in_map)
	maximum = in_map.calc_score()

	# initializes variable and empty lists for data and maps
	data = []
	steps = []

	# add first value
	data.append(maximum)

	# iterates over tries
	for i in range(tries_hill):

		# copies map
		try_map = copy.copy(best_map)

		# chooses which placement function to use
		if (hill_type == 0):

			try_map.random_swap_houses(nr_houses)
			folder = 'hillclimber'

		elif (hill_type == 1):

			try_map.tactical_swap_houses(nr_houses)
			folder = 'tactical_hillclimber'

		# calc score, update if greater than previous and append to data
		score = try_map.calc_score()
		if score > maximum:
			maximum = score
			best_map = try_map
		data.append(maximum)

		# saves visualization and appends each best map
		if save_steps == True:
			steps.append(copy.deepcopy(best_map))

	return {'best_map' : best_map, 'data' : data, 'steps' : steps}


if __name__ == '__main__':

	from __import__ import MAP_20, coloured_map, save_results, make_gif, \
						   best_of_random, plot_data

	random_map = best_of_random(MAP_20, 1, False)
	hillclimber_map = hillclimber(random_map['best_map'], 10, 1, 1)
	# tactical_hillclimber_map = hillclimber(MAP_20, 1, 10, 1, 1, True)
    #
	# plot_data(hillclimber_map['data'], 'hillclimber60', 'plot')
	# coloured_map(hillclimber_map['best_map'], 'hillclimber60', 'best')
	# save_results(hillclimber_map['data'], 'hillclimber60', 'data')
	# make_gif(hillclimber_map['steps'], 'hillclimber60', 'hillclimber')

	# plot_data(tactical_hillclimber_map['data'], 'tactical_hillclimber', 'plot')
	# coloured_map(hillclimber_map['best_map'], 'tactical_hillclimber', 'best')
	# save_results(hillclimber_map['data'], 'tactical_hillclimber', 'data')
	# make_gif(hillclimber_map['steps'], 'tactical_hillclimber', 'tactical_hillclimber')
