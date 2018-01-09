# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import copy


def greedy(nr_startmaps, map_specs, istep, save_steps = False):
	''' Random places water and greedy places house based on most freespace on the map.

	Input arguments:
	start_maps -- integer, how many random placed water begin maps of the function
	map_specs -- type specifications of the case, from file in folder specifications
	save_steps -- boolean, saving each step/map for visualization

	Returns dictionary containing:
	best_map -- object, best map
	data -- list of floats, scores of maps
	steps -- list of objects, all created maps

	Example: greedy(5, MAP_40, True)
	'''

	from __import__ import Map

	# initializes empty list for created maps
	total_maps = []

	# initialize score variable and best map
	score = 0
	steps = []
	data = []

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
			coordinates = total_maps[start_map].calc_freespace_on_map(istep)

			j = len(coordinates) - 1

			# place house where valid beginning with biggest freespace to smallest
			while (allowed == False):

				allowed = total_maps[start_map].place_house(0, coordinates[j])

				j += -1

			# check if minimum score is reached after 5 houses, otherwise continue to next map
			if (i == prune_house):

				minscore = total_maps[start_map].calc_score()

				# if minscore < 9000000:
				# 	break

			total_maps[start_map].calc_score()

			if save_steps == True:
				steps.append(copy.deepcopy(total_maps[start_map]))


		# calc score of created map
		tmpscore  = total_maps[start_map].calc_score()

		# update best score if greater
		if tmpscore > score:

			score = tmpscore
			best_map = total_maps[start_map]

		data.append(score)


	# returns created map and score
	return {'bestmap': best_map, 'data' : data, 'steps': steps}



if __name__ == '__main__':

	from __import__ import MAP_20, MAP_40, MAP_60, Map, coloured_map, \
						   plot_data, make_gif

	greedy_map = greedy(1, MAP_40, 5, True)
    #
	# coloured_map(best_random_map['best_map'], 'greedy60', 'best')
	# save_results(best_random_map['data'], 'greedy_present', 'data')
	# plot_data([greedy['data']], 'greedy_present', 'plot')
	make_gif(greedy_map['steps'], 'greedy40', 'greedy40')
