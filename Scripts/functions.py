# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

import os
from classes import *
from case import *
import numpy

'''
All basic functions to operate on the map.
'''

def place_house(ah_map, loc, house_id, type_charac):
    '''Places a one family house on location on the map, with a given id.'''

    ah_map.houses.append(House(house_id, type_charac, loc))

    return ah_map


def calc_freespace(newhouse, ah_map):

    # coordinates new house
    x_newhouse = newhouse.location['x']
    y_newhouse = newhouse.location['y']

    diff_housescurr = [0, 0]

    # calculate x and y difference new and first and calc freespace variable
    diff_housescurr[0] = ah_map.houses[0].location['x'] - x_newhouse
    diff_housescurr[1] = ah_map.houses[0].location['y'] - y_newhouse
    freespace = numpy.sqrt(numpy.power(diff_housescurr[0], 2) + numpy.power(diff_housescurr[1], 2))

    # iterate over all houses in map
    for house in ah_map.houses:

        if house.self_id != newhouse.self_id:
            # calculate x and y difference new and curr
            diff_housescurr[0] = house.location['x'] - x_newhouse
            diff_housescurr[1] = house.location['y'] - y_newhouse

            # calculates distance between new and current
            distancecurr = numpy.sqrt(numpy.power(diff_housescurr[0], 2) + numpy.power(diff_housescurr[1], 2))

            # update if freespace is greater than curr distance
            if freespace >= distancecurr:

            	freespace = distancecurr

    print (freespace)
    return freespace

def calc_freespaceforreal(newhouse, ah_map):

    # coordinates new house
    x_newhouse = newhouse.location['x']
    y_newhouse = newhouse.location['y']

    # corners coordinates new house
    corn_coornew = newhouse.corners

    # initiate variable list
    diff_housescurr = [0, 0]

    # difference between center and wall of house
    x_diffhouse = newhouse.charac['width'] / 2
    y_diffhouse = newhouse.charac['height'] / 2

    # calculate x and y difference new and first and calc freespace variable
    diff_housescurr[0] = ah_map.houses[0].location['x'] - x_newhouse
    diff_housescurr[1] = ah_map.houses[0].location['y'] - y_newhouse
    freespace = numpy.sqrt(numpy.power(diff_housescurr[0], 2) + numpy.power(diff_housescurr[1], 2))

    # iterate over all houses in map
    for house in ah_map.houses:

        if house.self_id != newhouse.self_id:

            distancecurr = 0
            # calculate x and y difference new and curr
            diff_housescurr[0] = house.location['x'] - x_newhouse
            diff_housescurr[1] = house.location['y'] - y_newhouse

            # check if coordinate falls within house - x range
            if house.location['x'] > corn_coornew['lb']['x'] and house.location['x'] < corn_coornew['rb']['x']:

            	freespace = diff_housescurr[0] - (newhouse.charac['width'] / 2)

            # check if coordinate falls within house - y range
            elif house.location['y'] > corn_coornew['lo']['y']and house.location['y'] < corn_coornew['lb']['y']:

            	freespace = diff_housescurr[1] - (newhouse.charac['height'] / 2)

            # check cornerdistance
            else:

                diff_housecorn = [0,0]

                distancelist = []

                # iterate over corners
                for i in corn_coornew:
                    for j in house.corners:

                        # calculate x and y difference between corners
                        diff_housecorn[0] = corn_coornew[i]['x'] - house.corners[j]['x']
                        diff_housecorn[1] = corn_coornew[i]['y'] - house.corners[j]['y']

                        # # calculate x and y difference between nextcorners
                        # diff_housescorn[3] = corn_coornew[i]['x'] - house.corners[j + 1]['x']
                        # diff_housescorn[4] = corn_coornew[i]['y'] - house.corners[j + 1]['y']

                        # calculates distance between curr two corners
                        distancecurrcorncurr = numpy.sqrt(numpy.power(diff_housecorn[0], 2) + numpy.power(diff_housecorn[1], 2))

                        distancelist.append(distancecurrcorncurr)

                        # # calculates distance between next two corners
                        # distancecurrcornnext = numpy.sqrt(numpy.power(diff_housescorn[3], 2) + numpy.power(diff_housescorn[4], 2))

                        # if distancecurrcorcurr > distancecurrcornnext:

                        # 	freespace = distancecurrcornnext



                        # diff corners
                        # distancecurr = numpy.sqrt(numpy.power(diff_housescurr[0], 2) + numpy.power(diff_housescurr[1], 2))

                        # # calculates distance between new and current
                        #    			distancecurr = numpy.sqrt(numpy.power(diff_housescurr[0], 2) + numpy.power(diff_housescurr[1], 2))


                    freespace = numpy.amin(distancelist)


            # # calculates distance between new and current
            # distancecurr = numpy.sqrt(numpy.power(diff_housescurr[0], 2) + numpy.power(diff_housescurr[1], 2))

            # # update if freespace is greater than curr distance
            # if freespace >= distancecurr:

            # 	freespace = distancecurr

    print (freespace)
    return freespace
