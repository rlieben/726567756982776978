# Group:        726567756982776978
# Assignment:   Amstelhaege

'''
First algorithm that places houses, used to test the classes of classes.py.
'''

from classes import *
from functions import *
from random import randint

def create_test():
    ah_map = Map(WIDTH_MAP, HEIGHT_MAP)

    for i in range(10):
        rand_y_loc = randint(0,HEIGHT_MAP - SIZE_1F[0])
        rand_x_loc = randint(0,WIDTH_MAP - SIZE_1F[1])

        loc = {'x':rand_x_loc,'y':rand_y_loc}

        house_id = i

        place_one_family(ah_map, loc, house_id)

    return ah_map

create_test()
