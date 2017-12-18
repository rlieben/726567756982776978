import copy


def greedy(nr_startmaps, map_specs, save_steps = False):
	''' Random places water and greedy places house based on most freespace on the map.

	Input arguments:
	start_maps -- integer, how many random placed water begin maps of the function
	map_specs -- type specifications of the case, from file in folder specifications
	save_steps -- boolean, saving each step/map for visualization

	Returns dictionary containing:
	best_map -- object, best map
	data -- list, scores of maps
	steps -- list, with all created maps

	Example: greedy(5, MAP_40, True)
	'''

	from __import__ import split, coloured_map

	# initializes empty list for created maps
	total_maps = []

	# initialize score variable and best map
	score = 0
	steps = []
	data = []
	l = 0

	# initialize house pruning point
	prune_house = 4

	# amount of runs for script
	for start_map in range(nr_startmaps):

		# initializes map
		total_maps.append(Map(map_specs))

		# places water on map
		k = 0

		while len(total_maps[start_map].water) < total_maps[0].max_waterbodies:
			total_maps[start_map].place_water_random()
			k += 1

		# iterates over houses
		for i in range(len(total_maps[start_map].construction)):

			allowed = False

			# get freespace coordinates on map
			coordinates = total_maps[start_map].calc_freespace_on_map()

			j = len(coordinates[0]) - 1

			# place house where valid beginning with biggest freespace to smallest
			while (allowed == False):

				allowed = total_maps[start_map].place_house(0, coordinates[0][j])

				j += -1

			# check if minimum score is reached after 5 houses, otherwise continue to next map
			if (i == prune_house):

				minscore = total_maps[start_map].calc_score()

				if (map_specs == MAP_20 and minscore < 6300000 or
					map_specs == MAP_40 and minscore < 9000000 or
					map_specs == MAP_60 and minscore < 7000000):

					break

			print(i)

			total_maps[start_map].calc_score()

			if save_steps == True:
				coloured_map(total_maps[start_map], 'greedy60' + split +
							 'tmp_gif', (str(l).zfill(3)))
				l += 1
				steps.append(total_maps[start_map])


		# calc score of created map
		tmpscore  = total_maps[start_map].calc_score()

		# update best score if greater
		if tmpscore > score:

			score = tmpscore
			best_map = total_maps[start_map]

		data.append(score)


	# returns created map and score
	return {'bestmap': best_map, 'data' : data, 'steps': total_maps}



if __name__ == '__main__':

	from __import__ import MAP_20, MAP_40, MAP_60, Map, coloured_map, plot_data, make_gif

	# greedy_map = greedy(5, MAP_60, True)
    #
	# plot_data([greedy['data']], 'greedy60', 'plot')
	# coloured_map(best_random_map['best_map'], 'greedy60', 'best')
	# save_results(best_random_map['data'], 'greedy60', 'data')
	make_gif([], 'greedy60', 'greedy60')
