
import sys
find_forward = sys.path[0].find('/')
find_backward = sys.path[0].find('\\')

if find_forward > find_backward:
	split = '/'
else:
	split = '\\'

list_dir = sys.path[0].split(split)
string = ''
for i in range(len(list_dir) - 1):
    string += list_dir[i]
    string += split

sys.path.insert(0, string)


from Classes.house import *
from Classes.map import *
from Classes.water import *
from Characteristics.Amstelhaege import *
from Algorithms.helpers import *
from Algorithms.best_of_random import *
from Algorithms.hillclimber import *
from Algorithms.tactical_hillclimber import *
from Algorithms.depthfirst import *
from Algorithms.particle_swarm import *
from Visuals.scatterplot import *
from Results.txtwriter import *

import numpy
import random
import copy
