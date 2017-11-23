# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Test script for Toon.
'''

from classes import *
from functions import *
from algorithms import *
from visuals import *


maximum = 0
best_map = random_generator()

for i in range(20):
    ah_map = random_generator()
    summy = 0
    for house in ah_map.houses:
        ah_map.calc_freespace(house)
        house.calc_value()
        summy += house.value

    if summy > maximum:
        maximum = summy
        best_map = ah_map

scatterplot(best_map)

print(maximum)

for i in range(10):
    ah_map = hill_climber(best_map)
    summy = 0
    for house in ah_map.houses:
        ah_map.calc_freespace(house)
        house.calc_value()
        summy += house.value
    print(i)

    if summy > maximum:
        maximum = summy
        best_map = ah_map

scatterplot(best_map)

print(maximum)
