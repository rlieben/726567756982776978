# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

class Map(object):
    '''Grid that keeps track of all the cells.'''

    def __init__(self, width, height):
        '''Grid is a list in a list (thus a matrix) filled with cells.
           Houses is a list containing all houses.
           Water is a list containint all water elements.'''

        self.houses = []
        self.water = []
        self.charac = {'width' : width, 'height' : height}

    def calc_freespace(self, newhouse):
        '''Takes a class house as input and calculates the minimum freespace of
           this house.'''

        # coordinates new house
        x_newhouse = newhouse.location['x']
        y_newhouse = newhouse.location['y']

        # initiate variable list
        diff_houses = [0, 0]

        # difference between center and wall of new house
        x_diffwall = newhouse.charac['width'] / 2
        y_diffwall = newhouse.charac['height'] / 2

        # creating temporary variable for freespace
        tmpfreespace = []


        # calculating distance to borders and adding to tmp freespace
        tmpfreespace.append(x_newhouse)
        tmpfreespace.append(y_newhouse)
        tmpfreespace.append(self.charac['width'] - x_newhouse)
        tmpfreespace.append(self.charac['height'] - y_newhouse)

        # iterate over all houses in map
        for house in self.houses:

            # skips itself
            if house.self_id != newhouse.self_id:


                # check if coordinate falls within house x - range
                if house.location['x'] > newhouse.corners['lb']['x'] \
                   and house.location['x'] < newhouse.corners['rb']['x']:

                    # save freespace between walls of houses
                	tmpfreespace.append(abs(diff_houses[0] \
                                        - x_diffwall
                                        - (house.charac['width'] / 2)))

                # check if coordinate falls within house y - range
                elif house.location['y'] > newhouse.corners['lo']['y'] \
                     and house.location['y'] < newhouse.corners['lb']['y']:

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
