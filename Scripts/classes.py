# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Code containing all classes used.
'''


class Map(object):
    '''Grid that keeps track of all the cells.'''

    def __init__(self, width, height):
        '''Houses is a list containing all houses.
           Water is a list containint all water elements.'''

        self.houses = []
        self.water = []
        self.measures = {'width' : width, 'height' : height}


class House(object):
    '''Basis for the three different house classes.'''

    def __init__(self, self_id, type_charac, loc):
        '''Location is the coordinate of the centre of the house.
           Freespace is the distance to the closest neighbour.
           Value is the value of the house.
           Charac is a dict filled with the characteristics of this type of
           house.'''

        self.self_id = self_id
        self.location = loc # loc is a dict {'x' : ..., 'y' : ...}
        self.freespace = 0
        self.value = 0
        self.charac = type_charac
        self.corners = self.find_corners()

    def calc_value(self, freespace):
        '''Calculates the value of this house.'''

        self.value = self.charac['start_value'] + (self.charac['start_value']
                     * (freespace - self.charac['min_free'])
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

        return [lb, rb, lo, ro]




class Water_Element(object):
    '''One of a maximum of four areas destinated for water.'''

    def __init__(self, width, length, loc):
        '''Location is coordinate of middle.
            Size is a dict with the width and length.'''

        self.location = loc
        self.size = {'width' : width, 'length' : length}
