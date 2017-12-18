# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import numpy
import copy


def force_move(in_map, tries, factor, save_steps = False):
	''' Forces a move in opposite direction of nearest house neighbour.

	Input arguments:
	in_map -- object, input map
	tries -- integer, number of moves for each house
	factor -- float, ....
	save_steps -- boolean, saving each step/map for visualization

	Returns dictionary containing:
	best_map -- object, best map
	data -- list, scores of maps
	steps -- list, with all created maps

	Example: force_move(in_map, 3, 0.5, True)
	'''

	from __import__ import split, coloured_map

	# calculate value for houses and map and copies map
	for house in in_map.houses:
		house.calc_value()
	in_map.calc_score()
	best_map = copy.copy(in_map)

	# initializes empty lists for data and maps
	data = []
	steps = []

	# initialize variables
	k = 0

	# iterate over tries
	for i in range(tries):

		# iterate over houses
		for j in range(len(best_map.houses)):

			# copy map and house
			out_map = copy.copy(best_map)
			house = out_map.houses[j]
			old_loc = house.location

			# remove house
			out_map.remove_house(j)

			# 
			a = numpy.random.uniform(0, factor)

			# set new location
			new_loc = {'x' : house.location['x'] + a * house.direction['x'],
				   	   'y' : house.location['y'] + a * house.direction['y']}

			# place house
			allowed = out_map.place_house(0, new_loc)

			# if place not valid, place on old loc
			if allowed == False:
				out_map.place_house(0, old_loc)

			# 
			data.append(best_map.score)

		# calc freespace and value
		for house in out_map.houses:
			house.calc_freespace(out_map)
			house.calc_value()

		# calc score of map and update if greater
		if out_map.calc_score() > best_map.score:
			best_map = out_map

		# saves visualization and appends each best map
		if save_steps == True:
			coloured_map(best_map, 'force_move60' + split + 'tmp_gif',
						 (str(k).zfill(3)))
			k += 1
			steps.append(best_map)

	return {'best_map' : best_map, 'data' : data, 'steps' : steps}


if __name__ == '__main__':

	from __import__ import MAP_20, random_generator, coloured_map, \
						   save_results, make_gif, plot_data, MAP_60

	random_map = random_generator(MAP_20)
	force_move_map1 = force_move(copy.copy(random_map), 10, 0.2)
	force_move_map2 = force_move(copy.copy(random_map), 10, 0.4)
	force_move_map3 = force_move(copy.copy(random_map), 10, 0.6)
	force_move_map4 = force_move(copy.copy(random_map), 10, 0.8)
	force_move_map5 = force_move(copy.copy(random_map), 10, 1.0)

	plot_data([force_move_map1['data'], force_move_map2['data'],
			   force_move_map3['data'], force_move_map4['data'],
			   force_move_map5['data']], '', 'plot_experiment')
	# plot_data([force_move_map['data']], 'force_move60', 'plot')
	# coloured_map(force_move_map['best_map'], 'fore_move60', 'best')
	# save_results(force_move_map['data'], 'force_move60', 'data')
	# make_gif(force_move_map['steps'], 'force_move60', 'force')
