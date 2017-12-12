
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

# input is empty map, output is value calculated
def hillclimber(map_charac, tries_random, tries_hill, nr_houses, hill_type):
	'''Moves, every iteration, houses for optimalization.

	Input arguments:
	map_charac -- object, map characteristics
	tries_random -- integer, number of random maps created
	tries_hill -- integer, number of hillclimbing
	nr_houses -- integer, nr of houses that are moved with each hillclimb
	hill_type -- type of hillclimber as integer(0: random, 1:based on freespace)
	'''

	best_map = best_of_random(map_charac, tries_random)
	maximum = best_map.calc_score()

	scatterplot(best_map, "best_of_random for tactical")
	print("score random:", maximum)

	data = [maximum]

	legelist = []

	for i in range(tries_hill):
		try_map = copy.copy(best_map)

		if (hill_type == 0):

			try_map.random_swap_houses(nr_houses)
		elif (hill_type == 1):

			try_map.tactical_swap_houses(nr_houses)
			print("iteration", i)
		else:
			print("type of hillclimber not specified/recognised.")

		score = try_map.calc_score()

		print("score: ", score)

		legelist.append(score)
		scatterplot(try_map, "tacticaltestplot" + str(i))

		if score > maximum:
			maximum = score
			best_map = try_map

			data.append(maximum)


	return {'map' : best_map, 'data' : legelist}
