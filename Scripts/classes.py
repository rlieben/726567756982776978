# Group:        726567756982776978
# Assignment:   Amstelhaege

'''
Code containing all classes used.
'''

WIDTH_MAP = 160
HEIGHT_MAP = 180
WATER_PREVALENCE = 0.20
NR_HOUSES = [20, 40, 60]
DISTR_HOUSES = [0.60, 0.25, 0.15] # [one_family, bungalow, mansion]

# variables of houses
VALUE_1F = 285000
PERC_1F = 3
MIN_FREESPACE_1F = 2
VALUE_BU = 399000
PERC_BU = 4
MIN_FREESPACE_BU = 3
VALUE_MA = 610000
PERC_MA = 6
MIN_FREESPACE_MA = 6



class Cell(object):
    '''One element in the grid.'''

    def __init__(self, x, y):
        '''Actual value is based on the houses on/around the cell.
           Possible value considers possible removal/placing of house.
           Type is the type of building/element placed on this cell.'''
        self.location = [x, y] # miss niet nodig
        self.actual_value = 0
        self.possible_value = 0
        self.type = 'Nothing'

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

    def __init___(self, height, width):
        '''Grid is a list in a list (thus a matrix) filled with cells.
           Houses is a list containing all houses.
           Water is a list containint all water elements.'''
        self.grid = [[Cell(x, y) for x in range(height)] for y in range(width)]
        self.houses = []
        self.water = []


class House(object):
    '''Basis for the three different house classes.'''

    def __init__(self, self_id):
        '''Structure is list of cells on which house is placed.
           Space is list of cells that fall within the range of closest
           neighbouring house.'''
        self.self_id = self_id
        self.structure = []
        self.space = []
        self.value = 0

    def add_house(self, x, y):
        '''Fills the structure list with cells.'''
        self.structure.append([x, y])


class One_Family(House):
    '''First of three types of houses.'''

    def __init__(self, self_id):
        '''Inherits from class House.'''
        super.__init__(self, self_id)

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
        super.__init__(self, self_id)

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
        super.__init__(self, self_id)

    def calc_value(freespace):
        '''Calculates the value of this mansion.'''

        # checks whether minimumspace is sufficient for extra value
        if (freespace - MIN_FREESPACE_MA) > 0:

            # factor of freespace between houses
            factor_freespace = ((freespace - MIN_FREESPACE_MA) * PERC_MA) / 100

            # end total value of one family house
            return VALUE_MA + (VALUE_MA * (factor_freespace)

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
