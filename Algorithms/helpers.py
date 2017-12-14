
from __import__ import *

import numpy
import matplotlib as mpl
import matplotlib.pyplot as plot
import matplotlib.patches as patches
import sys


def random_generator(map_charac):
	'''Generates a random map.'''

	out_map = Map(map_charac)

<<<<<<< HEAD
	# nr_water = 4
	# i = 0
    #
	# while len(out_map.water) < nr_water:
	# 	out_map.place_water(nr_water, i)
	# 	i += 1
    #
	# opp = 0
    #
	# for water in out_map.water:
	# 	opp = opp + (water.width * water.height)
    #
	# print(opp)
=======
	i = 0
	nr_water = 4

	# for i in range(nr_water):
	while len(out_map.water) < nr_water:
		out_map.place_water(nr_water, i)
		i += 1

>>>>>>> 885fb81582d45d81e304762fdcb14eaaab977961

	for i in range(len(out_map.construction)):

		index = int(numpy.random.uniform(0, len(out_map.construction) - 1))

		allowed = False
		while allowed == False:

			loc = {'x' : random.uniform(0, out_map.width),
				   'y' : random.uniform(0, out_map.height)}

			allowed = out_map.place_house(index, loc)

	return out_map
