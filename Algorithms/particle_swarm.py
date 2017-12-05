
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
from Algorithms.helpers import *
import random
import numpy
import copy


def particle_swarm_map(map_charac):

	out_map = random_generator(map_charac)
	directions = []

	for house in out_map.houses:
		freespace = house.calc_freespace()
		direction = {'x' : numpy.uniform(- freespace, freespace),
					 'y' : numpy.uniform(- freespace, freespace}

		house.location = {'x' : house.location['x'] + direction['x'],
						  'y' : house.location['y'] + direction['y']}

		directions.append(direction)
