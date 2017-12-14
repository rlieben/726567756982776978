
import numpy
import copy

from __import__ import coloured_map

def particle_swarm(in_map, tries, save_steps=False):

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
	particle_map = particle_swarm(random_map, 20, True)

	coloured_map(particle_map['best_map'], 'particle_swarm', 'best')
	save_results(particle_map['data'], 'particle_swarm', 'data')

	make_gif(particle_map['steps'], 'particle_swarm', 'particle')
