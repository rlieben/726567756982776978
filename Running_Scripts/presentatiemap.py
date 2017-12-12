
from __import__ import *
import copy

import matplotlib as mpl
import matplotlib.pyplot as plot
import numpy as np
import matplotlib.patches as patches
import sys


def scatterplot(ah_map, name):

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

	plot.savefig(name)

	plot.clf()



ah_map = Map(MAP_20)

scatterplot(ah_map, "presentatie map")

random_map = best_of_random(MAP_20, 1)

scatterplot(random_map, "presentatie random map")