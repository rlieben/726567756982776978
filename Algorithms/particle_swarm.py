
from __import__ import *

import matplotlib as mpl
import matplotlib.pyplot as plot
import numpy as np
import matplotlib.patches as patches
import sys


def particle_swarm(in_map, tries):

	for house in in_map.houses:
		house.calc_value()

	in_map.calc_score()

	best_map = copy.copy(in_map)

	data = []
	k = 0
	for i in range(tries):

		for j in range(len(best_map.houses)):

			out_map = copy.copy(best_map)

			house = out_map.houses[j]
			old_loc = house.location

			out_map.remove_house(j)

			a = numpy.random.uniform(0, 1)

			new_loc = {'x' : house.location['x'] + a * house.direction['x'],
				   	   'y' : house.location['y'] + a * house.direction['y']}

			allowed = out_map.place_house(0, new_loc)

			if allowed == False:
				out_map.place_house(0, old_loc)

			# scatterplot(out_map, str(k), 'TESTparticle')
			k += 1

		for house in out_map.houses:
			house.calc_freespace(out_map)
			house.calc_value()

		if out_map.calc_score() > best_map.score:
			best_map = copy.copy(out_map)
			data.append(best_map.score)

		# coloured_map(best_map, str(i), 'TESTparticle')


	return {'map' : best_map, 'data' : data}
