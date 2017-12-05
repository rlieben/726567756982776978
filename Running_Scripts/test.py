
<<<<<<< HEAD
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
from Algorithms.fireworks import *
from Algorithms.best_of_random import *
from Algorithms.hillclimber import *
from Visuals.scatterplot import *
=======
from __import__ import *
>>>>>>> db70d46db1d995c0fa7027e0022fa6804eedf112

# ah_map = Map(MAP_20)
# allowed = ah_map.place_house({'x' : 50, 'y' : 50}, 1, ah_map.types[0])
# print(allowed)
# allowed = ah_map.place_house({'x' : 50, 'y' : 40}, 2, ah_map.types[0])
# print(allowed)
#
# for house in ah_map.houses:
# 	print(house.freespace)
<<<<<<< HEAD

ah_map = random_generator(MAP_20)
=======
#
# ah_map = Map(MAP_20)
>>>>>>> db70d46db1d995c0fa7027e0022fa6804eedf112

fireworks(MAP_20)
