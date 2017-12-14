
from __import__ import House, Map

import numpy
import matplotlib as mpl
import matplotlib.pyplot as plot
import matplotlib.patches as patches
import sys


def random_generator(map_charac):
	'''Generates a random map.'''

	out_map = Map(map_charac)

	i = 0
	nr_water = 4

	while len(out_map.water) < 4:
		out_map.place_water_random(i, nr_water)
		i += 1

	for i in range(len(out_map.construction)):

		index = int(numpy.random.uniform(0, len(out_map.construction) - 1))

		allowed = False
		while allowed == False:

			loc = {'x' : random.uniform(0, out_map.width),
				   'y' : random.uniform(0, out_map.height)}

			allowed = out_map.place_house(index, loc)

	# # while len(out_map.water) < nr_water:
	# out_map.place_water(i, nr_water)

	return out_map
