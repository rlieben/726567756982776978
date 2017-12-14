
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

		p.append(patches.Rectangle((house.corners['lb']['x'],
									house.corners['lb']['y']),
									house.width, house.height,
									facecolor=house.colour))

	for water in ah_map.water:

		p.append(patches.Rectangle((water.corners['lb']['x'],
									water.corners['lb']['y']),
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



def scatterplot2(ah_map, name):

	data = []

	for i in range(len(ah_map.houses)):


		x = ah_map.houses[i].location['x']
		y = ah_map.houses[i].location['y']

		colors = (0, 0, 0)
		area = np.pi * 1

		data.append([ah_map.houses[i].corners['lb']['x'],
					 ah_map.houses[i].corners['lb']['y']])
		data.append([ah_map.houses[i].corners['lo']['x'],
					 ah_map.houses[i].corners['lo']['y']])
		data.append([ah_map.houses[i].corners['lo']['x'],
					 ah_map.houses[i].corners['lo']['y']])
		data.append([ah_map.houses[i].corners['ro']['x'],
					 ah_map.houses[i].corners['ro']['y']])
		data.append([ah_map.houses[i].corners['ro']['x'],
					 ah_map.houses[i].corners['ro']['y']])
		data.append([ah_map.houses[i].corners['rb']['x'],
					 ah_map.houses[i].corners['rb']['y']])
		data.append([ah_map.houses[i].corners['rb']['x'],
					 ah_map.houses[i].corners['rb']['y']])
		data.append([ah_map.houses[i].corners['lb']['x'],
					 ah_map.houses[i].corners['lb']['y']])

	for water in ah_map.water:
		print(water.width, water.height, water.self_id)
		data.append([water.corners['lb']['x'],
					 water.corners['lb']['y']])
		data.append([water.corners['lo']['x'],
					 water.corners['lo']['y']])
		data.append([water.corners['lo']['x'],
					 water.corners['lo']['y']])
		data.append([water.corners['ro']['x'],
					 water.corners['ro']['y']])
		data.append([water.corners['ro']['x'],
					 water.corners['ro']['y']])
		data.append([water.corners['rb']['x'],
					 water.corners['rb']['y']])
		data.append([water.corners['rb']['x'],
					 water.corners['rb']['y']])
		data.append([water.corners['lb']['x'],
					 water.corners['lb']['y']])

	axes = plot.gca()
	axes.set_xlim([0, ah_map.width])
	axes.set_ylim([0, ah_map.height])

	# for every value in data
	for i in range(0, len(data) - 1, 2):
		# define lists
		plot_array_x = []
		plot_array_y = []

		# append values in pairs to lists
		plot_array_x.append(data[i][0])
		plot_array_x.append(data[i + 1][0])
		plot_array_y.append(data[i][1])
		plot_array_y.append(data[i + 1][1])

		# plot each of these pairs seperately
		plot.plot(plot_array_x, plot_array_y, 'g')

	plot.savefig(name)


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
		scatterplot2(best_map, str(i))


	return {'map' : best_map, 'data' : data}
