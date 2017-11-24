# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

'''
Script containing all usable algorithms to place houses.
'''


from classes import *
from functions import *
from case import *
import random
import numpy

def random_generator():
    ah_map = Map(MAP['width'], MAP['height'])

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

            allowed = place_house(ah_map, loc, house_id, ONE_FAM)

    for i in range(BU):

        allowed = False

        while allowed == False:
            rand_y_loc = random.uniform(0,MAP['height'] - (BUNGALOW['height']/2))
            rand_x_loc = random.uniform(0,MAP['width'] - (BUNGALOW['width']/2))

            loc = {'x':rand_x_loc,'y':rand_y_loc}

            house_id = i

            allowed = place_house(ah_map, loc, house_id, BUNGALOW)

    for i in range(MA):

        allowed = False

        while allowed == False:
            rand_y_loc = random.uniform(0,MAP['height'] - (MANSION['height']/2))
            rand_x_loc = random.uniform(0,MAP['width'] - (MANSION['width']/2))

            loc = {'x':rand_x_loc,'y':rand_y_loc}

            house_id = i

            allowed = place_house(ah_map, loc, house_id, MANSION)

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
                                        - (tmp_houses[i].charac['height']/2))
            rand_x_loc = random.uniform(0, MAP['width']
                                        - (tmp_houses[i].charac['width']/2))

            loc = {'x':rand_x_loc,'y':rand_y_loc}

            allowed = place_house(ah_map, loc , tmp_houses[i].self_id,
                                  tmp_houses[i].charac)

    return ah_map

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
            loc = calc_freespace_on_map(ah_map, new_house)

            allowed = place_house(ah_map, loc , tmp_houses[i].self_id,
                                  tmp_houses[i].charac)

    return ah_map
