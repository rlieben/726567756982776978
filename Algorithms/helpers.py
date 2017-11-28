
import sys
list_dir = sys.path[0].split('\\')
string = ''
for i in range(len(list_dir) - 1):
    string += list_dir[i]
    string += '\\'

sys.path.insert(0, string)

from Classes.house_class import *
from Classes.map_class import *
from Classes.water_class import *
from Types.Characteristics_Amstelhaege import *
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

				house_id = i

				allowed = out_map.place_house(loc, house_id, ONE_FAM)

	return out_map

# input is empty map, output is value calculated
def random_swap_houses(in_map, nr_houses):
	'''Moves, every iteration, three houses for optimalization.

	Inout arguments:
	in_map -- input map
	'''

	tmp_index = []
	tmp_houses = []

	for i in range(nr_houses):
		tmp_index.append(int(numpy.random.uniform(0, len(in_map.houses) - 1)))

	for i in range(nr_houses):
		tmp_houses.append(in_map.houses[tmp_index[i]])
		del in_map.houses[tmp_index[i]]

	# add same amount of houses which were deleted
	for i in range(nr_houses):

		allowed = False

		while allowed == False:

			loc = {'x' : random.uniform(0, in_map.height),
				   'y' : random.uniform(0, in_map.width)}

			if tmp_houses[i].type == 'one_family':
				charac = ONE_FAM
			elif tmp_houses[i].type == 'bungalow':
				charac = BUNGALOW
			elif tmp_houses[i].type == 'mainsion':
				charac = MANSION

			allowed = in_map.place_house(loc , tmp_houses[i].self_id, charac)

	return in_map

def tactical_swap_houses(in_map, nr_houses):

	tmp_index = []
	tmp_houses = []

	for i in range(nr_houses):
		tmp_index.append(int(numpy.random.uniform(0, len(in_map.houses) - 1)))

	for i in range(nr_houses):
		tmp_houses.append(in_map.houses[tmp_index[i]])
		del in_map.houses[tmp_index[i]]

	for i in range(nr_houses):

		allowed = False

		while allowed == False:

			loc = in_map.calc_freespace_on_map(tmp_houses[i])

			if tmp_houses[i].type == 'one_family':
				charac = ONE_FAM
			elif tmp_houses[i].type == 'bungalow':
				charac = BUNGALOW
			elif tmp_houses[i].type == 'mainsion':
				charac = MANSION

			allowed = in_map.place_house(loc , tmp_houses[i].self_id, charac)

	return in_map
