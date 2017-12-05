# Group:        726567756982776978
# Assignment:   Amstelhaege

'''
First algorithm that places houses, used to test the classes of classes.py.
'''

from classes import *
from functions import *
from random import *
from premises import *


def create_test():
    ah_map = Map(MAP['width'], MAP['height'])


    OF = int(MAP['nr_houses'][0] * MAP['distr_houses'][0])
    BU = int(MAP['nr_houses'][0] * MAP['distr_houses'][1])
    MA = int(MAP['nr_houses'][0] * MAP['distr_houses'][2])

    for i in range(OF):
        rand_y_loc = randint(0,MAP['height'] - ONE_FAM['height'])
        rand_x_loc = randint(0,MAP['width'] - ONE_FAM['width'])

        loc = {'x':rand_x_loc,'y':rand_y_loc}

        house_id = i

        place_house(ah_map, loc, house_id, ONE_FAM)

    for i in range(BU):
        rand_y_loc = randint(0,MAP['height'] - BUNGALOW['height'])
        rand_x_loc = randint(0,MAP['height'] - BUNGALOW['height'])

        loc = {'x':rand_x_loc,'y':rand_y_loc}

        house_id = i

        place_house(ah_map, loc, house_id, BUNGALOW)

    for i in range(MA):
        rand_y_loc = randint(0,MAP['height'] - MANSION['height'])
        rand_x_loc = randint(0,MAP['height'] - MANSION['height'])

        loc = {'x':rand_x_loc,'y':rand_y_loc}

        house_id = i

        place_house(ah_map, loc, house_id, MANSION)

    return ah_map