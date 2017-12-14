
import numpy
import copy

from __import__ import coloured_map

def force_move(in_map, tries, save_steps=False):
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

	for house in in_map.houses:
		house.calc_value()

	in_map.calc_score()

	best_map = in_map
	data = []
	steps = []
	k = 0

	for i in range(tries):

		for j in range(len(best_map.houses)):

			out_map = copy.copy(best_map)

			house = out_map.houses[j]
			old_loc = house.location

			out_map.remove_house(j)

			a = numpy.random.uniform(0, 1)

			new_loc = {'x' : house.location['x'] + a * house.direction['x'],
				   	   'y' : house.location['y'] + a * house.direction['y']}

			allowed = out_map.place_house(0, new_loc)

			if allowed == False:
				out_map.place_house(0, old_loc)

		for house in out_map.houses:
			house.calc_freespace(out_map)
			house.calc_value()

		if out_map.calc_score() > best_map.score:
			best_map = out_map
			data.append(best_map.score)

		if save_steps == True:
			coloured_map(best_map, 'particle_swarm\\tmp_gif', (str(k).zfill(3)))
			k += 1
			steps.append(best_map)

	return {'best_map' : best_map, 'data' : data, 'steps' : steps}


if __name__ == '__main__':

	from __import__ import MAP_20, random_generator, coloured_map, \
						   save_results, make_gif

	random_map = random_generator(MAP_20)
	force_move_map = force_move(random_map, 20, True)

	coloured_map(force_move_map['best_map'], 'force_move', 'best')
	save_results(force_move_map['data'], 'force_move', 'data')

	make_gif(force_move_map['steps'], 'force_move', 'force')
