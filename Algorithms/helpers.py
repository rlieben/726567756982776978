
import sys
list_dir = sys.path[0].split('\\')
string = ''
for i in range(len(list_dir) - 1):
    string += list_dir[i]
    string += '\\'

sys.path.insert(0, string)

from Classes.house import *
from Classes.map import *
from Classes.water import *
from Characteristics.Amstelhaege import *
import random
import numpy


def random_generator(map_charac):
	'''Generates a random map.'''

	out_map = Map(map_charac)

	for i in range(len(out_map.distr_houses)):

		nr_of_type = out_map.nr_houses * out_map.distr_houses[i]

		for j in range(int(nr_of_type)):

			allowed = False

			while allowed == False:
				loc = {'x' : random.uniform(0, out_map.height),
					   'y' : random.uniform(0, out_map.width)}

				house_id = 100 * (j + 1) + i

				allowed = out_map.place_house(loc, house_id,
											  map_charac['types_houses'][i])

	return out_map
