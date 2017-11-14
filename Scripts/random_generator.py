# Group:        726567756982776978
# Assignment:   Amstelhaege

'''
First algorithm that places houses, used to test the classes of classes.py.
'''

from classes import *
from functions import *
from random import *


def create_test():
    ah_map = Map(WIDTH_MAP, HEIGHT_MAP)

    OF = 13
    BU = 4
    MA = 3

    for i in range(OF):
        rand_y_loc = randint(0,HEIGHT_MAP - SIZE_1F[0])
        rand_x_loc = randint(0,WIDTH_MAP - SIZE_1F[1])

        loc = {'x':rand_x_loc,'y':rand_y_loc}

        house_id = i

        place_one_family(ah_map, loc, house_id)

    for i in range(BU):
        rand_y_loc = randint(0,HEIGHT_MAP - SIZE_BU[0])
        rand_x_loc = randint(0,WIDTH_MAP - SIZE_BU[1])
        print(rand_x_loc)

        loc = {'x':rand_x_loc,'y':rand_y_loc}

        house_id = i

        place_bungalow(ah_map, loc, house_id)

    for i in range(MA):
        rand_y_loc = randint(0,HEIGHT_MAP - SIZE_MA[0])
        rand_x_loc = randint(0,WIDTH_MAP - SIZE_MA[1])

        loc = {'x':rand_x_loc,'y':rand_y_loc}

        house_id = i

        place_mansion(ah_map, loc, house_id)

    return ah_map
