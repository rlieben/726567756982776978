
from __import__ import *

def particle_swarm_map(map_charac, tries):

	print('1')
	out_map = random_generator(map_charac)

	print('in')

	data = []

	for i in range(tries):
		for house in out_map.houses:
			house.calc_freespace(out_map)
			freespace = house.freespace
			house.direction = {'x' : random.uniform(- freespace, freespace),
						 	   'y' : random.uniform(- freespace, freespace)}

			loc = {'x' : house.location['x'] + house.direction['x'],
				   'y' : house.location['y'] + house.direction['y']}

			house_id = house.self_id
			type_charac = out_map.types[house.index_nr]
			del house

			allowed = out_map.place_house(loc, house_id, type_charac)

			print(i)

		for house in out_map.houses:
			house.calc_value()

		data.append(out.map.calc_score())

	return {'map' : out_map, 'data' : data}
