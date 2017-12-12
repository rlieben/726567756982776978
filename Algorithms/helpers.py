
from __import__ import *


def random_generator(map_charac):
	'''Generates a random map.'''

	out_map = Map(map_charac)
	i = 0

	out_map.place_water(i)


	for k in range(len(out_map.distr_houses)):

		nr_of_type = out_map.nr_houses * out_map.distr_houses[i]

		for j in range(int(nr_of_type)):

			allowed = False

			while allowed == False:
				loc = {'x' : random.uniform(0, out_map.width),
					   'y' : random.uniform(0, out_map.height)}

				house_id = 100 * (i + 1) + j

				allowed = out_map.place_house(loc, house_id,
											  map_charac['types_houses'][i])
		i -=1
	return out_map
