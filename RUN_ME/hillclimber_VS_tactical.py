
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
from Algorithms.hillclimber import *
from Algorithms.tactical_hillclimber import *
from Visuals.scatterplot import *

best_random = hillclimber(MAP_20, 10, 10, 1)
print('hillclimber:', best_random.score)

best_hill = tactical_hillclimber(MAP_20, 10, 10, 1)
print('tactical:', best_hill.score)
