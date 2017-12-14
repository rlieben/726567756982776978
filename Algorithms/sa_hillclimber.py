from __import__ import *

import numpy


# input is empty map, output is value calculated
def sa_hillclimber(map_charac, tries_random, nr_houses, hill_type):
	'''Moves, every iteration, houses for optimalization.

	Input arguments:
	map_charac -- object, map characteristics
	tries_random -- integer, number of random maps created
	tries_hill -- integer, number of hillclimbing
	nr_houses -- integer, nr of houses that are moved with each hillclimb
	hill_type -- type of hillclimber as integer(0: random, 1:based on freespace)
	'''

	MIN = 1
	temp = 10
	cooling_rate = 0.3

	best_map = best_of_random(map_charac, tries_random)
	maximum = best_map.calc_score()

	scatterplot(best_map, "best_of_random for tactical", "TESTsa")
	print("score random:", maximum)

	data = [maximum]

	legelist = []

	i = 0

	while temp > MIN:

		try_map = copy.copy(best_map)

		if (hill_type == 0):

			try_map.random_swap_houses(nr_houses)
		elif (hill_type == 1):

			try_map.tactical_swap_houses(nr_houses) # swap type....
			print("iteration", i)
		else:
			print("type of hillclimber not specified/recognised.")

		score = try_map.calc_score()

		print("score: ", score)

		legelist.append(score)
		scatterplot(try_map, "tacticaltestplot" + str(i), "TESTsa")
		i += 1

		if score > maximum or \
		   numpy.exp((maximum - score) / temp) > numpy.random.uniform(0, 1):
			maximum = score
			best_map = try_map

			data.append(maximum)

		temp *= (1 - cooling_rate)


	return {'map' : best_map, 'data' : legelist}
