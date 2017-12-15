import copy


def greedy(start_maps, map_charac):
	''' Random places water and greedy places house based on most freespace.

	Input arguments:
	start_maps -- integer, how many different begin maps of the function
	nr_waterbodies -- integer, number of waterbodies that need to be placed
	map_charac -- file with specifications of the case

	Returns dictionary containing:
	best_map -- object, best map
	score -- float, score of best map
	steps -- object, all created maps
	'''

	# initializes empty list for created maps
	total_maps = []

	# initialize score variable and best map
	score = 0
	best_map = []

	# initialize house pruning point
	prune_house = 4

	# amount of runs for script
	for start_map in range(start_maps):

		print("start map: ", start_map)
		# initializes map
		total_maps.append(Map(map_charac))

		# places water on map
		k = 0

		while len(total_maps[start_map].water) < total_maps.max_waterbodies:
			total_maps[start_map].place_water_random(total_maps.max_waterbodies)
			k += 1

		# iterates over houses
		for i in range(len(total_maps[start_map].construction)):


			print("test", len(total_maps[start_map].construction))

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

				if (map_charac == MAP_20 and minscore < 6300000 or
					map_charac == MAP_40 and minscore < 9000000 or
					map_charac == MAP_60 and minscore < 7000000):

					print(" ")
					break

			total_maps[start_map].calc_score()
			print("score", total_maps[start_map].score)

			coloured_map(total_maps[start_map], "greedy", "greedy" + str(start_map) + str(i))


		# calc score of created map
		tmpscore  = total_maps[start_map].calc_score()



		# update best score if greater
		if tmpscore > score:

			score = tmpscore
			best_map = total_maps[start_map]

	# returns created map and score
	return {'bestmap': best_map, 'score' : score, 'steps': total_maps}



if __name__ == '__main__':

	from __import__ import MAP_20, MAP_40, MAP_60, Map, coloured_map, plot_data

	greedy_map = greedy(20, MAP_20)

	plot_data(greedy['data'], 'force_move', 'plot')
	# coloured_map(best_random_map['best_map'], 'best_of_random', 'best')
	# save_results(best_random_map['data'], 'best_of_random', 'data')
	# make_gif(best_random_map['steps'], 'best_of_random', 'random')
