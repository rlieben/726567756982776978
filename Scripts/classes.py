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
        '''Grid is a list in a list (thus a matrix) filled with cells.
           Houses is a list containing all houses.
           Water is a list containint all water elements.'''

        self.houses = []
        self.water = []
        self.measures = {'width' : width, 'height' : height}


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
        self.corners = self.find_corners()
        self.freespace = 0
        self.value = 0
        self.charac = type_charac


    def calc_value(self, freespace):
        '''Calculates the value of this house.'''

        self.value = self.charac['start_value'] + (self.charac['start_value']
                     * (freespace - self.charac['min_free'])
                     * self.charac['perc'])

    def find_corners(self):
        lb = {'x':(self.location['x'] - 0.5 * self.charac['width']),'y':(self.location['y'] + 0.5 * self.charac['height'])}
        rb = {'x':(self.location['x'] + 0.5 * self.charac['width']),'y':(self.location['y'] + 0.5 * self.charac['height'])}
        lo = {'x':(self.location['x'] - 0.5 * self.charac['width']),'y':(self.location['y'] - 0.5 * self.charac['height'])}
        ro = {'x':(self.location['x'] + 0.5 * self.charac['width']),'y':(self.location['y'] - 0.5 * self.charac['height'])}
        return [lb, rb, lo, ro]




class Water_Element(object):
    '''One of a maximum of four areas destinated for water.'''

    def __init__(self, loc):
        '''Water is a list of cells on which water is placed.'''

        self.location = loc
        self.size = ''
