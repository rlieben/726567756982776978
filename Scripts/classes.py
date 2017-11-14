# Study:      Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Code containing all classes used.
'''


class Cell(object):
    '''One element in the grid.'''

    def __init__(self):
        '''Actual value is based on the houses on/around the cell.
           Possible value considers possible removal/placing of house.
           Type is the type of building/element placed on this cell.'''
        self.actual_value = 0
        self.possible_value = 0
        self.type = 'empty'

    def calc_actual_value(self):
        '''Based on the locations of houses around, value is changed.'''
        print('TODO: class Cell, calc_actual_value')
        # self.actual_value = function

    def calc_possible_value(self):
        '''Takes in account the possible removal/placing of new house.'''
        print('TODO: class Cell, calc_possible_value')
        # self.possible_value = function


class Map(object):
    '''Grid that keeps track of all the cells.'''

    def __init__(self, width, height):
        '''Grid is a list in a list (thus a matrix) filled with cells.
           Houses is a list containing all houses.
           Water is a list containint all water elements.'''
        self.grid = [[Cell() for x in range(height)] for y in range(width)]
        self.houses = []
        self.water = []
        self.measures = {'width' : width, 'height' : height}


class House(object):
    '''Basis for the three different house classes.'''

    def __init__(self, self_id, type_charac):
        '''Structure is list of cells on which house is placed.
           Space is list of cells that fall within the range of closest
           neighbouring house.'''
        self.self_id = self_id
        # ipv hele list een locatie gebruiken
        self.structure = []
        self.space = []
        self.value = 0
        self.type_charac = type_charac

    def add_structure(self, loc):
        self.structure.append(loc)


class One_Family(House):
    '''First of three types of houses.'''

    def __init__(self, self_id):
        '''Inherits from class House.'''
        super().__init__(self_id)

    def calc_value(freespace):
        '''Calculates the value of this one family home.'''

        # checks whether minimumspace is sufficient for extra value
        if (freespace - MIN_FREESPACE_1F) > 0:

            # factor of freespace between houses
            factor_freespace = ((freespace - MIN_FREESPACE_1F) * PERC_1F) / 100

            # end total value of one family house
            return VALUE_1F + (VALUE_1F * factor_freespace)

        else:

            return VALUE_1F

        # super.value = function()


class Bungalow(House):
    '''Second of three types of houses.'''

    def __init__(self, self_id):
        '''Inherits from class House.'''
        super().__init__(self_id)

    def calc_value(freespace):
        '''Calculates the value of this bungalow.'''

        # checks whether minimumspace is sufficient for extra value
        if (freespace - MIN_FREESPACE_BU) > 0:

            # factor of freespace between houses
            factor_freespace = ((freespace - MIN_FREESPACE_BU) * PERC_BU) / 100

            # end total value of one family house
            return VALUE_BU + (VALUE_BU * factor_freespace)

        else:

            return VALUE_BU


    # super.value = function


class Mansion(House):
    '''Last of three types of houses.'''

    def __init__(self, self_id):
        '''Inherits from class House.'''
        super().__init__(self_id)

    def calc_value(freespace):
        '''Calculates the value of this mansion.'''
        # checks whether minimumspace is sufficient for extra value
        if (freespace - MIN_FREESPACE_MA) > 0:

            # factor of freespace between houses
            factor_freespace = ((freespace - MIN_FREESPACE_MA) * PERC_MA) / 100

            # end total value of one family house
            return VALUE_MA + (VALUE_MA * factor_freespace)

        else:

            return VALUE_MA

    # super.value = function


class Water_Element(object):
    '''One of a maximum of four areas destinated for water.'''

    def __init__(self):
        '''Water is a list of cells on which water is placed.'''
        self.water = []

    def place_water(self, location):
        '''Fills the water list with cells.'''
        self.water.append(location)
