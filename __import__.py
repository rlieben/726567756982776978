# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import sys

# depending on OS, different symbols are used to seperate folders
# this checks which symbol is used
find_forward = sys.path[0].find('/')
find_backward = sys.path[0].find('\\')

if find_forward > find_backward:
	split = '/'
else:
	split = '\\'

string = sys.path[0] + split

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
from Algorithms.simulated_annealing import sa_hillclimber
from Visualisations.coloured_map import coloured_map
from Visualisations.txtwriter import save_results
from Visualisations.make_gif import make_gif
from Visualisations.plot_data import plot_data
