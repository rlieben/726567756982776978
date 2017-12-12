
from __import__ import *
import numpy

def random_generator(map_charac):
	'''Generates a random map.'''

	out_map = Map(map_charac)

	for i in range(len(out_map.construction)):

		index = int(numpy.random.uniform(0, len(out_map.construction) - 1))

		allowed = False
		while allowed == False:

			loc = {'x' : random.uniform(0, out_map.width),
				   'y' : random.uniform(0, out_map.height)}

			allowed = out_map.place_house(index, loc)

	return out_map
