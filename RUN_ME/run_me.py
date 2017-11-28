# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Does 100 random ways to lay 20 houses on the map and shows the best solution.
'''

# from classes import *
# from functions import *
# from visuals import *
# from algorithms import *



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
from Algorithms.algorithms import *
from Visuals.scatterplot import *



maximum = 0
best_map = random_generator()

for i in range(1):
    ah_map = random_generator()
    summy = 0
    for house in ah_map.houses:
        house.calc_freespace(ah_map)
        house.calc_value()
        summy += house.value

    if summy > maximum:
        maximum = summy
        best_map = ah_map

scatterplot(best_map)

print(maximum)

for i in range(1):
    ah_map = hill_climber(best_map)
    summy = 0
    for house in ah_map.houses:
        house.calc_freespace(ah_map)
        house.calc_value()
        summy += house.value
    print(i)

    if summy > maximum:
        maximum = summy
        best_map = ah_map

scatterplot(best_map)

print(maximum)
