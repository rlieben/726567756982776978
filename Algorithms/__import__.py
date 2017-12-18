# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

'''Creates proper system paths, so the algorithms can access other folders.'''

import sys

# depending on OS, different symbols are used to seperate folders
# this checks which symbol is used
find_forward = sys.path[0].find('/')
find_backward = sys.path[0].find('\\')

if find_forward > find_backward:
	split = '/'
else:
	split = '\\'

# split the first system path at previously found symbol
list_dir = sys.path[0].split(split)

# init string to create new system path
string = ''

# reassemble system path, but not untill end
for i in range(len(list_dir) - 1):
    string += list_dir[i]
    string += split

# insert newly assembled system path to list of system paths
sys.path.insert(0, string)

# import all funtions from folders
from Classes.house import House
from Classes.map import Map
from Classes.water import Water
from Specifications.amstelhaege import MAP_20, MAP_40, MAP_60
from Algorithms.helpers import random_generator
from Algorithms.best_of_random import best_of_random
from Algorithms.hillclimber import hillclimber
from Algorithms.greedy import greedy
from Algorithms.force_move import force_move
from Visualisations.coloured_map import coloured_map
from Visualisations.txtwriter import txtwriter
from Visualisations.make_gif import make_gif
from Visualisations.plot_data import plot_data
