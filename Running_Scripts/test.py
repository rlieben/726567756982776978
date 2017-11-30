
import sys
list_dir = sys.path[0].split('/')
string = ''
for i in range(len(list_dir) - 1):
    string += list_dir[i]
    string += '/'

sys.path.insert(0, string)

from Classes.house import *
from Classes.map import *
from Classes.water import *
from Characteristics.Amstelhaege import *
from Algorithms.helpers import *
from Algorithms.best_of_random import *
from Algorithms.hillclimber import *
from Visuals.scatterplot import *

ah_map = Map(MAP_20)
allowed = ah_map.place_house({'x' : 50, 'y' : 50}, 1, ah_map.types[0])
print(allowed)
allowed = ah_map.place_house({'x' : 45, 'y' : 45}, 2, ah_map.types[0])
print(allowed)

for house in ah_map.houses:
	print(house.freespace)

scatterplot(ah_map)
