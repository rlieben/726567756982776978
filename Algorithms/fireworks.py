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


def fireworks(map_charac):

    def max_val(iters):

        max_val = 0
        max_val_houses = []

        for i in range(iters):
            map_max_val = random_generator(map_charac)

            for house in map_max_val.houses:
                house.calc_freespace(map_max_val)
                value = house.calc_value()

                allowed = False
                # check if house value is higher than previous value and store in max_val
                # and check if location is not the same. add characteristics of house in list
                if value > max_val:
                    max_val = value
                    max_val_houses.append(house)

            new_map = Map(map_charac)

            for house in max_val_houses:
                print(house.type)
                new_map.place_house(house.location, house.self_id, house.type)

            return new_map

    max_val(1)

    i = 2

    # place number of houses - houses placed with max_values
    while (out_map.nr_houses) - (len(max_val_houses)) > 0:

        out_map = max_val(1)

        for house in max_val_houses:

            nr_of_type = out_map.nr_houses * out_map.distr_houses[i] 

        for j in range(int(nr_of_type)):

        	allowed = False

        	while allowed == False:
        		loc = {'x' : random.uniform(0, out_map.width),
        			   'y' : random.uniform(0, out_map.height)}

        		house_id = 100 * (i + 1) + j

        		allowed = out_map.place_house(loc, house_id,
        									  map_charac['types_houses'][i])
        i -= 1


    return max_val, out_map
