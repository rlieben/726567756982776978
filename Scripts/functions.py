# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

from classes import *
import numpy

'''
All basic functions to operate on the map.
'''

def place_house(ah_map, loc, house_id, type_charac):
    '''Places a one family house on location on the map, with a given id.'''

    # adds class to list of houses in the map
    # for i in range(house_id - 1):
    #     free_space = loc['x'][i] - loc['x'][i + 1]
    #     if free_space > ONE_FAM['min_free']
    ah_map.houses.append(House(house_id, type_charac, loc))

    return ah_map



# def calc_score(ah_map):
#         '''Calculates the score of the map.'''
#
#         for house in ah_map.houses:
#
#             freespace = 0
#             for cor in house.structure:
#                 for other in ah_map.houses:
#                     for other_cor in other.structure:
#                         if cor != other_cor:
#                             tmp = numpy.sqrt(numpy.power(cor['x']
#                                   - other_cor['x'], 2) + numpy.power(cor['y']
#                                   - other_cor['y'], 2))
#                             if tmp < freespace:
#                                 freespace = tmp
#
#             house.calc_value(freespace)
#
#         score = 0
#         for house in ah_map.houses:
#             score += house.value
#
#         return score
