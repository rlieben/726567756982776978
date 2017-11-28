# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

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


    def calc_freespace(self, in_map):
        '''Takes a class house as input and calculates the minimum freespace of
           this house.'''

        # coordinates new house
        x_newhouse = self.location['x']
        y_newhouse = self.location['y']

        # initiate variable list
        diff_houses = [0, 0]

        # difference between center and wall of new house
        x_diffwall = self.charac['width'] / 2
        y_diffwall = self.charac['height'] / 2

        # creating temporary variable for freespace
        tmpfreespace = []


        # calculating distance to borders and adding to tmp freespace
        tmpfreespace.append(x_newhouse)
        tmpfreespace.append(y_newhouse)
        tmpfreespace.append(self.charac['width'] - x_newhouse)
        tmpfreespace.append(self.charac['height'] - y_newhouse)

        # iterate over all houses in map
        for house in in_map.houses:

            # skips itself
            if house.self_id != self.self_id:


                # check if coordinate falls within house x - range
                if house.location['x'] > self.corners['lb']['x'] \
                   and house.location['x'] < self.corners['rb']['x']:

                    # save freespace between walls of houses
                    tmpfreespace.append(abs(diff_houses[0] \
                                        - x_diffwall
                                        - (house.charac['width'] / 2)))

                # check if coordinate falls within house y - range
                elif house.location['y'] > self.corners['lo']['y'] \
                     and house.location['y'] < self.corners['lb']['y']:

                    # save freespace between walls of houses
                    tmpfreespace.append(abs(diff_houses[1] \
                                        - y_diffwall
                                        - (house.charac['height'] / 2)))

                # else compute distance of corners of the house
                else:

                    # create corner variable
                    diff_corners = [0,0]

                    # create distance variable list
                    distancelist = []

                    # iterate over corners of both houses
                    for i in self.corners:

                        for j in house.corners:

                            # calculate x and y difference between corners
                            diff_corners[0] = self.corners[i]['x'] \
                                              - house.corners[j]['x']

                            diff_corners[1] = self.corners[i]['y'] \
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
        self.freespace = freespace
