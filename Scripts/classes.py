# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

import numpy

'''
Code containing all classes used.
'''


class Map(object):
    '''Grid that keeps track of all the cells.'''

    def __init__(self, width, height):
        '''Grid is a list in a list (thus a matrix) filled with cells.
           Houses is a list containing all houses.
           Water is a list containint all water elements.'''

        self.houses = []
        self.water = []
        self.measures = {'width' : width, 'height' : height}

    def calc_freespace(self, newhouse):
        '''Takes a class house as input and calculates the minimum freespace of this house.'''

        # coordinates new house
        x_newhouse = newhouse.location['x']
        y_newhouse = newhouse.location['y']

        # initiate variable list
        diff_houses = [0, 0]

        # difference between center and wall of new house
        x_diffwall = newhouse.charac['width'] / 2
        y_diffwall = newhouse.charac['height'] / 2

        # calculate x and y difference new and first and calc first freespace variable
        diff_houses[0] = self.houses[0].location['x'] - x_newhouse
        diff_houses[1] = self.houses[0].location['y'] - y_newhouse
        freespace = numpy.sqrt(numpy.power(diff_houses[0], 2)
                    + numpy.power(diff_houses[1], 2))

        # iterate over all houses in map
        for house in self.houses:

            # skips itself
            if house.self_id != newhouse.self_id:

                # creating temporary variable for freespace
                tmpfreespace = []

                # calculate x and y difference new and current house
                diff_houses[0] = house.location['x'] - x_newhouse
                diff_houses[1] = house.location['y'] - y_newhouse

                # check if coordinate falls within house x - range
                if house.location['x'] > newhouse.corners['lb']['x'] \
                   and house.location['x'] < newhouse.corners['rb']['x']:

                    # save freespace between walls of houses
                	tmpfreespace.append(diff_houses[0] \
                                        - x_diffwall
                                        - (house.charac['width'] / 2))
                # check if coordinate falls within house y - range
                elif house.location['y'] > newhouse.corners['lo']['y'] \
                     and house.location['y'] < newhouse.corners['lb']['y']:

                    # save freespace between walls of houses
                	tmpfreespace.append(diff_houses[1] \
                                        - y_diffwall
                                        - (house.charac['height'] / 2))
                # else compute distance of corners of the house
                else:

                    # create corner variable
                    diff_corners = [0,0]

                    # create distance variable list
                    distancelist = []

                    # iterate over corners of both houses
                    for i in newhouse.corners:

                        for j in house.corners:

                            # calculate x and y difference between corners
                            diff_corners[0] = newhouse.corners[i]['x'] \
                                              - house.corners[j]['x']
                            
                            diff_corners[1] = newhouse.corners[i]['y'] \
                                              - house.corners[j]['y']

                            # calculates distance between curr two corners
                            distancecorn = numpy.sqrt(numpy.power( \
                                                      diff_corners[0], 2) \
                                                      + numpy.power( \
                                                      diff_corners[1], 2)) \
                            # save distance
                            distancelist.append(distancecorn)
                        # take the minimum distance
                        tmpfreespace.append(numpy.amin(distancelist))
                # take the minimum freespace
                freespace = numpy.amin(tmpfreespace)
        # set freespace of class
        newhouse.freespace = freespace


class House(object):
    '''Basis for the three different house classes.'''

    def __init__(self, self_id, type_charac, loc):
        '''Structure is list of cells on which house is placed.
           Space is list of cells that fall within the range of closest
           neighbouring house.
           Charac is a dict filled with the characteristics of this type of
           house.'''

        self.self_id = self_id
        self.location = loc # loc is a dict {'x' : ..., 'y' : ...}
        self.freespace = 0
        self.charac = type_charac
        self.corners = self.find_corners()
        self.freespace = 0
        self.value = 0



    def calc_value(self):
        '''Calculates the value of this house.'''

        self.value = self.charac['start_value'] + (self.charac['start_value']
                     * (self.freespace - self.charac['min_free'])
                     * self.charac['perc'])


    def find_corners(self):

        lb = {'x' : (self.location['x'] - 0.5 * self.charac['width']),
              'y' : (self.location['y'] + 0.5 * self.charac['height'])}

        rb = {'x' : (self.location['x'] + 0.5 * self.charac['width']),
              'y' : (self.location['y'] + 0.5 * self.charac['height'])}

        lo = {'x' : (self.location['x'] - 0.5 * self.charac['width']),
              'y' : (self.location['y'] - 0.5 * self.charac['height'])}

        ro = {'x' : (self.location['x'] + 0.5 * self.charac['width']),
              'y' : (self.location['y'] - 0.5 * self.charac['height'])}

        return {'lb' : lb, 'rb': rb, 'lo': lo, 'ro': ro}



class Water_Element(object):
    '''One of a maximum of four areas destinated for water.'''

    def __init__(self, loc):
        '''Water is a list of cells on which water is placed.'''

        self.location = loc
        self.size = ''
