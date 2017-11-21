# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Does 100 random ways to lay 20 houses on the map and shows the best solution.
'''

from classes import *
from functions import *
from visuals import *
from algorithms import *



maximum = 0
best_map = random_generator()

for i in range(100):
    ah_map = random_generator()
    summy = 0
    for house in ah_map.houses:
        ah_map.calc_freespace(house)
        house.calc_value()
        # print(house.charac['type'])
        # print(house.value)
        summy += house.value

    print("SUM")
    print(summy)

    if summy > maximum:
        maximum = summy
        best_map = ah_map

print("MAX")
print(maximum)

scatterplot(best_map)
