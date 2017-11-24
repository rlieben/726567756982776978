# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Test script for Luc.
'''

from classes import *
from functions import *
from algorithms import *
from visuals import *

def calc_av_freespace(ah_map):
    summy = 0
    for houses in ah_map.houses:
        summy += house.freespace - house.charac['min_free']

    return summy / len(ah_map.houses)


maximum = 0
best_map = random_generator()

for i in range(20):
    ah_map = random_generator()
    summy = 0
    for house in ah_map.houses:
        ah_map.calc_freespace(house)
        house.calc_value()
        summy += house.value
    if calc_av_freespace(ah_map) > 1:
        summy = summy / calc_av_freespace(ah_map)

    # print(calc_av_freespace(ah_map))
    # print(summy)

    if summy > maximum:
        maximum = summy
        best_map = ah_map

scatterplot(best_map)

print(maximum)

for i in range(100):
    ah_map = tactical_hill_climber(best_map)
    summy = 0
    for house in ah_map.houses:
        ah_map.calc_freespace(house)
        house.calc_value()
        summy += house.value

    if summy > (maximum * 0.99):
        maximum = summy
        best_map = ah_map

scatterplot(best_map)

print(maximum)
