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
from Algorithms.best_of_random import *
from Algorithms.helpers import *
import random
import numpy
import copy

max_val = 0
max_val_houses = []

# place 1 to 20 houses
for i in range (MAP['nr_houses'][0]):
    # get max value of house in random map
    for i in range(10):
        map_max_val = random_generator(MAP_20)
        for house in map_max_val.houses:
            house.calc_freespace(map_max_val)
            print(house.freespace)
            value = house.calc_value()
            print(value)

            # check if house value is higher than previous value and store in max_val
            # add characteristics of house in list
            if value > max_val:
                max_val = value
                max_val_houses.append(house)

    for house in max_val_houses:
        place_house(house)

    for i in range(MAP['nr_houses'][0] - len(max_val_houses)):
        place_house(random)




    # return max_val
