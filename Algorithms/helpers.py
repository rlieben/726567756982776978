
from __import__ import Map

# import house weggehaald

import numpy


def random_generator(map_charac):
	'''Generates a random map.'''

	out_map = Map(map_charac)

	nr_water = 4

	while len(out_map.water) < 4:
		out_map.place_water_random(nr_water)

	for i in range(len(out_map.construction)):

		index = int(numpy.random.uniform(0, len(out_map.construction) - 1))

		allowed = False
		while allowed == False:

			loc = {'x' : numpy.random.uniform(0, out_map.width),
				   'y' : numpy.random.uniform(0, out_map.height)}

			allowed = out_map.place_house(index, loc)

	# out_map.place_water(nr_water)

	return out_map
