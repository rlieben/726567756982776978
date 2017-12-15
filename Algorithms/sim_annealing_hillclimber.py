from __import__ import *

import numpy


# input is empty map, output is value calculated
def sa_hillclimber(map_charac, tries_random, nr_houses, hill_type, cooling_rate,
				   factor, save_steps = False):
	'''Moves, every iteration, houses for optimalization.

	Input arguments:
	map_charac -- file with specifications of the case
	tries_random -- integer, number of random maps created
	nr_houses -- integer, nr of houses that are moved with each hillclimb
	hill_type -- type of hillclimber as integer(0: random, 1:based on freespace)

	Output:
	dict containing: object, map with best map and list, data with scores of maps
	'''

	from __import__ import split, coloured_map

	MIN = 0.1
	temp = 1 - cooling_rate
	k = 0
	steps = []

	best_map = best_of_random(map_charac, tries_random)['best_map']
	maximum = best_map.calc_score()

	data = []

	i = 0

	while temp > MIN:

		try_map = copy.copy(best_map)

		if (hill_type == 0):

			try_map.random_swap_houses(nr_houses)

		elif (hill_type == 1):

			try_map.tactical_swap_houses(nr_houses) # swap type....


		score = try_map.calc_score()

		i += 1

		sim_annealin_value = (1 / numpy.pi) * numpy.arctan((score - maximum) / \
							  ((1 - temp) * maximum)) + (1 / 2)

		sim_annealin_value += factor * numpy.pi * (sim_annealin_value - 0.5)

		if score > maximum or sim_annealin_value > numpy.random.uniform(0, 1):
			maximum = score
			best_map = try_map

			data.append(maximum)

		if save_steps == True:
			coloured_map(best_map, 'sim_annealing_hillclimber' + split +
						 'tmp_gif', str(k).zfill(3))
			k += 1
			steps.append(best_map)

		temp *= (1 - cooling_rate)


	return {'best_map' : best_map, 'data' : data, 'steps' : steps}

if __name__ == '__main__':

	from __import__ import MAP_20, coloured_map, save_results, make_gif, \
						   best_of_random

	sa_hillclimber_map1 = sa_hillclimber(MAP_20, 10, 1, 0, 0.01, 1)
	sa_hillclimber_map2 = sa_hillclimber(MAP_20, 10, 1, 0, 0.01, 2)
	sa_hillclimber_map3 = sa_hillclimber(MAP_20, 10, 1, 0, 0.01, 3)
	sa_hillclimber_map4 = sa_hillclimber(MAP_20, 10, 1, 0, 0.01, 4)
	sa_hillclimber_map5 = sa_hillclimber(MAP_20, 10, 1, 0, 0.01, 5)

	plot_data([sa_hillclimber_map1['data'], sa_hillclimber_map2['data'],
		sa_hillclimber_map3['data'], sa_hillclimber_map4['data'],
		sa_hillclimber_map5['data']], '', 'experiment3')

	# coloured_map(sa_hillclimber_map['best_map'], 'sim_annealing_hillclimber', 'best')
	# save_results(sa_hillclimber_map['data'], 'sim_annealing_hillclimber', 'data')
	# make_gif(sa_hillclimber_map['steps'], 'sim_annealing_hillclimber', 'sa_hillclimber_map')
