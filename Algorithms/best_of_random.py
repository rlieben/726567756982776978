
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
from Algorithms.helpers import *
from Visuals.scatterplot import *

def best_of_random(map_charac, tries):

	maximum = 0
	best_map = random_generator(map_charac)

	for i in range(tries):
	    try_map = random_generator(map_charac)
	    summy = 0
	    for house in try_map.houses:
	        house.calc_freespace(try_map)
	        house.calc_value()
	        summy += house.value

	    if summy > maximum:
	        maximum = summy
	        best_map = try_map

	best_map.score = maximum
	return best_map
