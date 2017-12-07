
from __import__ import *

import matplotlib as mpl
import matplotlib.pyplot as plot
import numpy as np
import matplotlib.patches as patches
import sys


def scatterplot(ah_map, name, directory):

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

	for i in range(len(ah_map.water)):
		data.append([ah_map.water[i].corners['lb']['x'],
					 ah_map.water[i].corners['lb']['y']])
		data.append([ah_map.water[i].corners['lo']['x'],
					 ah_map.water[i].corners['lo']['y']])
		data.append([ah_map.water[i].corners['lo']['x'],
					 ah_map.water[i].corners['lo']['y']])
		data.append([ah_map.water[i].corners['ro']['x'],
					 ah_map.water[i].corners['ro']['y']])
		data.append([ah_map.water[i].corners['ro']['x'],
					 ah_map.water[i].corners['ro']['y']])
		data.append([ah_map.water[i].corners['rb']['x'],
					 ah_map.water[i].corners['rb']['y']])
		data.append([ah_map.water[i].corners['rb']['x'],
					 ah_map.water[i].corners['rb']['y']])
		data.append([ah_map.water[i].corners['lb']['x'],
					 ah_map.water[i].corners['lb']['y']])

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

	# plot.savefig(name)

	split = sys.path[1][2]
	list_dir = sys.path[0].split(split)
	string = ''
	for i in range(len(list_dir) - 1):
		string += list_dir[i]
		string += split

	plot.savefig(string + 'Results' + split + directory + split + name)

	plot.clf()

	# return plot.show()


def particle_swarm_map(map_charac, tries):

	out_map = random_generator(map_charac)

	data = []
	k = 0
	for i in range(tries):

		for j in range(len(out_map.houses) - 1):

			# print('old location: ', i, out_map.houses[j].location)

			out_map.houses[j].calc_freespace(out_map)

			freespace = out_map.houses[j].freespace

			copy_house = copy.copy(out_map.houses[j])

			out_map.houses[j].direction = {'x' : random.uniform(- freespace,
																freespace),
						 	   			   'y' : random.uniform(- freespace,
										   						freespace)}

			loc = {'x' : out_map.houses[j].location['x'] +
						 out_map.houses[j].direction['x'],
				   'y' : out_map.houses[j].location['y'] +
				   		 out_map.houses[j].direction['y']}

			del out_map.houses[j]

			allowed = out_map.place_house(loc, out_map.houses[j].self_id,
									  out_map.types[out_map.houses[j].index_nr])

			if allowed == False:
				out_map.houses.append(copy_house)
			scatterplot(out_map, str(k), 'TESTparticle')
			k += 1

		for house in out_map.houses:
			house.calc_value()

		data.append(out_map.calc_score())

		# scatterplot(out_map, str(i), 'TESTparticle')

	return {'map' : out_map, 'data' : data}
