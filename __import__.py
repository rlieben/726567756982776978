
import sys
find_forward = sys.path[0].find('/')
find_backward = sys.path[0].find('\\')

if find_forward > find_backward:
	split = '/'
else:
	split = '\\'

list_dir = sys.path[0].split(split)
string = ''
for i in range(len(list_dir)):
    string += list_dir[i]
    string += split

from Classes.house import *
from Classes.map import *
from Classes.water import *
from Specifications.amstelhaege import *
from Algorithms.helpers import *
from Algorithms.best_of_random import *
from Algorithms.hillclimber import *
from Algorithms.greedy import *
from Algorithms.force_move import *
from Visualisations.coloured_map import *
from Visualisations.txtwriter import *
from Visualisations.make_gif import *
from Visualisations.plot_data import *
