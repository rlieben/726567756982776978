# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


from classes import *
from functions import *
from premises import *
import random

<<<<<<< HEAD
def random():
=======
'''
First algorithm that places houses, used to test the classes of classes.py.
'''

def create_test():
>>>>>>> af4b6a19e3ba2dece4cdbf2c9e4a257eaaec22a2
    ah_map = Map(MAP['width'], MAP['height'])


    OF = int(MAP['nr_houses'][0] * MAP['distr_houses'][0])
    BU = int(MAP['nr_houses'][0] * MAP['distr_houses'][1])
    MA = int(MAP['nr_houses'][0] * MAP['distr_houses'][2])

    for i in range(OF):
        rand_y_loc = random.uniform(0,MAP['height'] - (ONE_FAM['height']/2))
        rand_x_loc = random.uniform(0,MAP['width'] - (ONE_FAM['width']/2))

        loc = {'x':rand_x_loc,'y':rand_y_loc}

        house_id = i

        place_house(ah_map, loc, house_id, ONE_FAM)

    for i in range(BU):
        rand_y_loc = random.uniform(0,MAP['height'] - (BUNGALOW['height']/2))
        rand_x_loc = random.uniform(0,MAP['width'] - (BUNGALOW['width']/2))

        loc = {'x':rand_x_loc,'y':rand_y_loc}

        house_id = i

        place_house(ah_map, loc, house_id, BUNGALOW)

    for i in range(MA):
        rand_y_loc = random.uniform(0,MAP['height'] - (MANSION['height']/2))
        rand_x_loc = random.uniform(0,MAP['width'] - (MANSION['width']/2))

        loc = {'x':rand_x_loc,'y':rand_y_loc}

        house_id = i

        place_house(ah_map, loc, house_id, MANSION)

    return ah_map
