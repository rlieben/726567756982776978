# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import numpy
import copy


# input is empty map, output is value calculated
def sa_hillclimber(in_map, nr_houses, hill_type, cooling_rate, factor,
				   save_steps = False):

	'''Moves a number of houses with simulated annealing.

	Input arguments:
	in_map -- object, map to hillclimb
	tries_hill -- integer, number times of hillclimbing
	nr_houses -- integer, number of houses to swap
	hill_type -- integer, type of hillclimber (0 : random,
											   1 : based on most freespace)
	factor -- float, number determing how strict the algorithm is when accepting
			  or declining a new value (higher = stricter)
	save_steps -- boolean, saving each step/map for visualization

	Returns dictionary containing:
	best_map -- object, best map
	data -- list of floats, scores of maps
	steps -- list of objects, all created maps

	Example: hillclimber(MAP_20, 40, 5, 1, True)
	'''

	# initialize variables and empyt lists for created maps and scores
	MIN = 0.1
	temp = 10 - cooling_rate
	steps = []
	data = []

	# copy input map as current best map
	best_map = copy.deepcopy(in_map)
	maximum = in_map.calc_score()

	# add first value
	data.append(maximum)

	# keep trying as long as minimal temperature has not been met
	while temp > MIN:

		# copy current best map
		try_map = copy.copy(best_map)

		# choose if heuristic is used (1)
		if (hill_type == 0):

			try_map.random_swap_houses(nr_houses)

		elif (hill_type == 1):

			try_map.tactical_swap_houses(nr_houses)


		score = try_map.calc_score()

		# determine value for annealing
		sim_annealin_value = (1 / numpy.pi) * numpy.arctan((score - maximum) / \
							  ((1 - temp) * maximum)) + (1 / 2)

		sim_annealin_value += factor * numpy.pi * (sim_annealin_value - 0.5)

		# test if new score is better then previous
		if score > maximum:
			maximum = score
			best_map = try_map

		# if not, see if it is accepted with annealing
		elif sim_annealin_value > numpy.random.uniform(0, 1):
			maximum = score
			best_map = try_map

			data.append(maximum)

		# add map to steps
		if save_steps == True:
			steps.append(copy.deepcopy(best_map))

		# adjust temperature
		temp *= (1 - cooling_rate)


	return {'best_map' : best_map, 'data' : data, 'steps' : steps}


if __name__ == '__main__':

	from __import__ import MAP_20, MAP_40, MAP_60, coloured_map, save_results, \
						   make_gif, best_of_random, plot_data


	random_map = best_of_random(MAP_20, 10, False)
	sa_hillclimber_map = sa_hillclimber(random_map['best_map'], 1, 0, 0.01, 14)

	plot_data([sa_hillclimber_map['data']], 'simulated_annealing', 'test')

	coloured_map(sa_hillclimber_map['best_map'], 'simulated_annealing', 'best')
	save_results(sa_hillclimber_map['data'], 'simulated_annealing', 'data')
	# make_gif(sa_hillclimber_map['steps'], 'simulated_annealing',
	# 		 'simulated_annealing')
