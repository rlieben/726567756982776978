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

    def calc_freespaceforreal(self, newhouse):

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
        diff_housescurr[0] = self.houses[0].location['x'] - x_newhouse
        diff_housescurr[1] = self.houses[0].location['y'] - y_newhouse
        freespace = numpy.sqrt(numpy.power(diff_housescurr[0], 2) + numpy.power(diff_housescurr[1], 2))

        # iterate over all houses in map
        for house in self.houses:

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

        newhouse.freespace = freespace
        # return freespace


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

class Water_Element(object):
    '''One of a maximum of four areas destinated for water.'''

    def __init__(self, loc):
        '''Water is a list of cells on which water is placed.'''

        self.location = loc
        self.size = ''
