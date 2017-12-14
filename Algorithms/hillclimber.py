
import copy


def hillclimber(map_charac, tries_random, tries_hill, nr_houses, hill_type,
				save_steps):
	'''Moves, every iteration, houses for optimalization.

	Input arguments:
	map_charac -- object, map characteristics
	tries_random -- integer, number of random maps created
	tries_hill -- integer, number of hillclimbing
	nr_houses -- integer, nr of houses that are moved with each hillclimb
	hill_type -- type of hillclimber as integer(0: random, 1:based on freespace)
	'''

	best_map = best_of_random(map_charac, tries_random)['best_map']
	maximum = best_map.calc_score()

	data = []
	steps = []

	for i in range(tries_hill):

		try_map = copy.copy(best_map)

		if (hill_type == 0):

			try_map.random_swap_houses(nr_houses)

		elif (hill_type == 1):

			try_map.tactical_swap_houses(nr_houses) # swap type....


		score = try_map.calc_score()

		if score > maximum:
			maximum = score
			best_map = try_map

		data.append(maximum)

		if save_steps == True:
			steps.append(best_map)

	return {'best_map' : best_map, 'data' : data, 'steps' : steps}


if __name__ == '__main__':

	from __import__ import MAP_20, coloured_map, save_results, make_gif

	hillclimber_map = hillclimber(MAP_20, 1, 10, 1, 0, True)

	coloured_map(hillclimber_map['best_map'], 'hillclimber', 'best')
	save_results(hillclimber_map['data'], 'hillclimber', 'data')

	make_gif(hillclimber_map['steps'], 'hillclimber', 'hillclimber')
