
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
from Algorithms.best_of_random import *
from Algorithms.hill_climber import *
from Visuals.scatterplot import *

best_random = best_of_random(MAP_20, 100)
print('best random:', best_random.score)

best_hill = hill_climber(MAP_20, 10, 100, 1)
print('hillclimber:', best_hill.score)
