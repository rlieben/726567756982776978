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

    summy = 0
    maximum = 0

    for house in ah_map.houses:
        ah_map.calc_freespace(house)
        house.calc_value()
        # print(house.charac['type'])
        # print(house.value)
        if house.value < 0:
            print(house.value)
        summy += house.value

    if summy > maximum:
        maximum = summy
        best_map = ah_map

    return maximum, best_map
