
from __import__ import *

import matplotlib as mpl
import matplotlib.pyplot as plot
import numpy as np
import matplotlib.patches as patches
import sys



def scatterplot(ah_map, name, directory):

	import matplotlib.patches as patches

	out_plot = plot.figure()
	ax = out_plot.add_subplot(111, aspect='equal')

	p = []

	for house in ah_map.houses:

		p.append(patches.Rectangle((house.location['x'], house.location['y']),
									house.width, house.height,
									facecolor=house.colour))

	for water in ah_map.water:

		p.append(patches.Rectangle((water.location['x'], water.location['y']),
									water.width, water.height,
									facecolor='blue'))


	for patch in p:
	    ax.add_patch(patch)

	axes = plot.gca()
	ax.set_facecolor('green')
	axes.set_xlim([0, ah_map.width])
	axes.set_ylim([0, ah_map.height])

	# out_plot.savefig(name)

	split = sys.path[1][2]
	list_dir = sys.path[0].split(split)
	string = ''
	for i in range(len(list_dir) - 1):
		string += list_dir[i]
		string += split

	out_plot.savefig(string + 'Results' + split + directory + split + name)

	out_plot.clf()

	# return out_plot.show()


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

		scatterplot(best_map, str(i), 'TESTparticle')


	return {'map' : best_map, 'data' : data}
