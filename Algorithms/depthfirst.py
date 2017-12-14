import copy


def depthfirst(start_maps, map_charac):
	''' Places house random and searches for the best child.

	Input arguments:
	start_maps -- integer, how many different begin maps of the function

	Returns:
	ah_map -- best map with 20 houses
	score -- score of best map
	'''

	# initializes map
	ah_map = Map(map_charac)

	# initialize score variables
	tempscore = 0
	score = 0

	# amount of runs for script
	for start_map in range(start_maps):

		# iterates over houses
		for i in range(len(ah_map.construction)):


			print("test", len(ah_map.construction))

			# sets house id
			# house_id = 100 * (int(j) + 1) + i

			allowed = False

			# get freespace coordinates on map
			coordinates = ah_map.calc_freespace_on_map()

			j = len(coordinates) - 1

			# place house where valid beginning with biggest freespace to smallest
			while (allowed == False):

				allowed = ah_map.place_house(0, coordinates[j])

				j += -1

			ah_map.calc_score()
			print("score of map after nr houses:", ah_map.score, i)
			coloured_map(ah_map, "greedy", "greedy" + str(i))



		# calc score of created map

		tmpscore  = ah_map.calc_score()



		# update best score if greater
		if tmpscore > score:

			score = tmpscore

	# returns created map and score
	return {'map': ah_map, 'score' : score}


def depthfirstwater(start_maps, nr_waterbodies, map_charac):
	''' Places house random and searches for the best child.

	Input arguments:
	start_maps -- integer, how many different begin maps of the function

	Returns:
	ah_map -- best map with 20 houses
	score -- score of best map
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

		while len(total_maps[start_map].water) < nr_waterbodies:
			total_maps[start_map].place_water(nr_waterbodies, k)
			k += 1

		# iterates over houses
		for i in range(len(total_maps[start_map].construction)):


			print("test", len(total_maps[start_map].construction))

			allowed = False

			# get freespace coordinates on map
			coordinates = total_maps[start_map].calc_freespace_on_map()

			j = len(coordinates) - 1

			# place house where valid beginning with biggest freespace to smallest
			while (allowed == False):

				allowed = total_maps[start_map].place_house(0, coordinates[j])

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

	print("hoi")

	from __import__ import MAP_20, MAP_40, MAP_60, Map, coloured_map

	# best_depthfirst = depthfirst(1, MAP_60)
	# print('best depthfirst:', best_depthfirst['map'].score)

	best_depthfirst = depthfirstwater(20, 4, MAP_20)
	print('best depthfirst:', best_depthfirst['map'].score)

	make_gif(best_depthfirst['steps'], 'greedy', 'greedy')


