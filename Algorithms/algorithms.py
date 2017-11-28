# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

'''
Script containing all usable algorithms to place houses.
'''


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
# from Algorithms.algorithms import *
import random
import numpy

def random_generator():
	ah_map = Map(MAP)

	OF = int(MAP['nr_houses'][0] * MAP['distr_houses'][0])
	BU = int(MAP['nr_houses'][0] * MAP['distr_houses'][1])
	MA = int(MAP['nr_houses'][0] * MAP['distr_houses'][2])

	for i in range(OF):

		allowed = False

		while allowed == False:
			rand_y_loc = random.uniform(0,MAP['height'] - (ONE_FAM['height']/2))
			rand_x_loc = random.uniform(0,MAP['width'] - (ONE_FAM['width']/2))

			loc = {'x':rand_x_loc,'y':rand_y_loc}

			house_id = i

			allowed = ah_map.place_house(loc, house_id, ONE_FAM)

	for i in range(BU):

		allowed = False

		while allowed == False:
			rand_y_loc = random.uniform(0,MAP['height'] - (BUNGALOW['height']/2))
			rand_x_loc = random.uniform(0,MAP['width'] - (BUNGALOW['width']/2))

			loc = {'x':rand_x_loc,'y':rand_y_loc}

			house_id = i

			allowed = ah_map.place_house(loc, house_id, BUNGALOW)

	for i in range(MA):

		allowed = False

		while allowed == False:
			rand_y_loc = random.uniform(0,MAP['height'] - (MANSION['height']/2))
			rand_x_loc = random.uniform(0,MAP['width'] - (MANSION['width']/2))

			loc = {'x':rand_x_loc,'y':rand_y_loc}

			house_id = i

			allowed = ah_map.place_house(loc, house_id, MANSION)

	return ah_map

# input is empty map, output is value calculated
def hill_climber(ah_map):

	CHANGE = 1
	tmp_index = []
	tmp_houses = []

	for i in range(CHANGE):
		tmp_index.append(int(numpy.random.uniform(0, len(ah_map.houses) - 1)))
    # print(tmp_index)

	for i in range(CHANGE):
		tmp_houses.append(ah_map.houses[tmp_index[i]])
		del ah_map.houses[tmp_index[i]]

    # add same amount of houses which were deleted
	for i in range(CHANGE):

		allowed = False

		while allowed == False:
			rand_y_loc = random.uniform(0, MAP['height']
			                            - (tmp_houses[i].height/2))
			rand_x_loc = random.uniform(0, MAP['width']
			                            - (tmp_houses[i].width/2))

			loc = {'x':rand_x_loc,'y':rand_y_loc}

			if tmp_houses[i].type == 'one_family':
				charac = ONE_FAM
			elif tmp_houses[i].type == 'bungalow':
				charac = BUNGALOW
			elif tmp_houses[i].type == 'mainsion':
				charac = MANSION

			allowed = ah_map.place_house(loc , tmp_houses[i].self_id, charac)

	return ah_map

	place_house(self, loc, house_id, type_charac)

def tactical_hill_climber(ah_map):

	CHANGE = 1
	tmp_index = []
	tmp_houses = []

	for i in range(CHANGE):
		tmp_index.append(int(numpy.random.uniform(0, len(ah_map.houses) - 1)))
	# print(tmp_index)

	for i in range(CHANGE):
		tmp_houses.append(ah_map.houses[tmp_index[i]])
		del ah_map.houses[tmp_index[i]]

	# add same amount of houses which were deleted
	for i in range(CHANGE):

		allowed = False

		while allowed == False:
			loc = calc_freespace_on_map(ah_map, tmp_houses[i])

			if tmp_houses[i].type == 'one_family':
				charac = ONE_FAM
			elif tmp_houses[i].type == 'bungalow':
				charac = BUNGALOW
			elif tmp_houses[i].type == 'mainsion':
				charac = MANSION

			allowed = ah_map.place_house(loc , tmp_houses[i].self_id, charac)

	return ah_map
