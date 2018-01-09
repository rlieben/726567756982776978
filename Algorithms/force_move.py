# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import numpy
import copy


def force_move(in_map, tries, max_fact, save_steps = False):
	''' Forces a move in opposite direction of nearest neighbour.

	Input arguments:
	in_map -- object, input map
	tries -- integer, number of moves for each house
	max_fact -- float, factor of freespace that is the maxium step size
	save_steps -- boolean, saving each step/map for visualization

	Returns dictionary containing:
	best_map -- object, best map
	data -- list of floats, scores of maps
	steps -- list of objects, with all created maps

	Example: force_move(in_map, 3, 0.5, True)
	'''

	# calculate value for houses and map and copies map
	for house in in_map.houses:
		house.calc_value()
	in_map.calc_score()
	best_map = copy.copy(in_map)

	maximum = in_map.score

	# initializes empty lists for data and maps
	data = []
	steps = []

	# add first value
	data.append(maximum)

	# iterate over tries
	for i in range(tries):

		# iterate over houses
		for j in range(len(best_map.houses)):

			# copy map
			out_map = copy.copy(best_map)

			# take house of list and save old location for later
			house = out_map.houses[j]
			old_loc = house.location

			# remove house
			out_map.remove_house(j)

			# takes random factor
			fact = numpy.random.uniform(0, max_fact)

			# set new location
			new_loc = {'x' : house.location['x'] + fact * house.direction['x'],
				   	   'y' : house.location['y'] + fact * house.direction['y']}

			# try to place house
			allowed = out_map.place_house(0, new_loc)

			# if placing not valid, return house to old location
			if allowed == False:
				out_map.place_house(0, old_loc)

		# append score to data
		data.append(best_map.score)

		# calc freespace and value
		for house in out_map.houses:
			house.calc_freespace(out_map)
			house.calc_value()

		# calc score of map and update if greater
		if out_map.calc_score() > best_map.score:
			best_map = out_map

		# append best map to visualization
		if save_steps == True:
			steps.append(copy.deepcopy(best_map))

	return {'best_map' : best_map, 'data' : data, 'steps' : steps}


if __name__ == '__main__':

	from __import__ import MAP_20, MAP_40, MAP_60, random_generator, \
						   coloured_map, save_results, make_gif, plot_data, \
						   best_of_random

	random_map = best_of_random(MAP_20, 1, False)
	force_move_map = force_move(random_map['best_map'], 10, 0.5, True)

	# plot_data([force_move_map['data'], '', 'plot_experiment')
	# plot_data([force_move_map['data']], 'force_move60', 'plot')
	# coloured_map(force_move_map['best_map'], 'fore_move60', 'best')
	# save_results(force_move_map['data'], 'force_move60', 'data')
	# make_gif(force_move_map['steps'], 'force_move_test', 'force')
