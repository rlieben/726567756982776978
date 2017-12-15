
import numpy
import copy


def force_move(in_map, tries, factor, save_steps = False):
	''' Forces a move by nearest house neighbour in opposite direction.

	Input arguments:
	in_map -- object, input map
	tries -- int, number of moves for each house
	save_steps -- boolean, for saving maps for visualization

	Output:
	dict -- containing  object, best_map with best map,
						list, data with map score and
						list, steps with all created maps
	'''

	from __import__ import split, coloured_map

	for house in in_map.houses:
		house.calc_value()

	in_map.calc_score()

	best_map = copy.copy(in_map)
	data = []
	steps = []
	k = 0

	for i in range(tries):

		for j in range(len(best_map.houses)):

			out_map = copy.copy(best_map)

			house = out_map.houses[j]
			old_loc = house.location

			out_map.remove_house(j)

			a = numpy.random.uniform(0, factor)

			new_loc = {'x' : house.location['x'] + a * house.direction['x'],
				   	   'y' : house.location['y'] + a * house.direction['y']}

			allowed = out_map.place_house(0, new_loc)

			if allowed == False:
				out_map.place_house(0, old_loc)

			data.append(best_map.score)

		for house in out_map.houses:
			house.calc_freespace(out_map)
			house.calc_value()

		if out_map.calc_score() > best_map.score:
			best_map = out_map


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
