# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import numpy


def random_generator(map_specs):
	'''Generates a random map.

	Input arguments:
	map_specs -- type specifications of the case, from file in folder specifications

	Returns:
	out_map -- object, output map

	Example: random_generator(MAP_60)
	'''

	from __import__ import House, Map

	# creates empty map
	out_map = Map(map_specs)

	# sets number of waterbodies
	nr_water = map_specs['nr_waterbodies']

	# randomly places water bodies
	while len(out_map.water) < out_map.max_waterbodies:
		out_map.place_water_random()

	# iterates over construction houses
	for i in range(len(out_map.construction)):

		# selects random house from construction list and places on random location
		index = int(numpy.random.uniform(0, len(out_map.construction) - 1))
		allowed = False
		while allowed == False:

			loc = {'x' : numpy.random.uniform(0, out_map.width),
				   'y' : numpy.random.uniform(0, out_map.height)}

			allowed = out_map.place_house(index, loc)

	# out_map.place_water(nr_water)

	return out_map
