
from __import__ import *

def particle_swarm_map(map_charac, tries):

	out_map = random_generator(map_charac)

	data = []

	for i in range(tries):
		for j in range(len(out_map.houses)):

			out_map.houses[j].calc_freespace(out_map)
			freespace = out_map.houses[j].freespace
			out_map.houses[j].direction = {'x' : random.uniform(- freespace, freespace),
						 	   'y' : random.uniform(- freespace, freespace)}

			loc = {'x' : out_map.houses[j].location['x'] + out_map.houses[j].direction['x'],
				   'y' : out_map.houses[j].location['y'] + out_map.houses[j].direction['y']}

			house_id = out_map.houses[j].self_id
			print(house_id)
			type_charac = out_map.types[out_map.houses[j].index_nr]

			del out_map.houses[j]

			allowed = out_map.place_house(loc, house_id, type_charac)

		print(i)

		for house in out_map.houses:
			house.calc_value()

		data.append(out.map.calc_score())

	return {'map' : out_map, 'data' : data}
