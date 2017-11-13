# Group:        726567756982776978
# Assignment:   Amstelhaege

'''
Code containing all classes used at application.py
'''

class Cell(object):
    '''One element in the grid.'''

    def __init__(self, x, y):
        '''Actual value is based on the houses on/around the cell.
           Possible value considers possible removal/placing of house.
           Type is the type of building/element placed on this cell.'''
        self.location = [x, y]
        self.actual_value = 0
        self.possible_value = 0
        self.type = ''

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
        '''Grid is a list in a list (thus a matrix) filled with cells.'''
        self.grid = [[Cell for x in range(height)] for y in range(width)]


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

    def add_house(self, location):
        '''Fills the structure list with cells.'''
        self.structure.append(location)


class One_Family(House):
    '''First of three types of houses.'''

    def __init__(self, self_id):
        '''Inherits from class House.'''
        super.__init__(self, self_id)

    def calc_value(self):
        '''Calculates the value of this one family home.'''
        print('TODO: class House, calc_value')
        # super.value = function


class Bugalow(House):
    '''Second of three types of houses.'''

    def __init__(self, self_id):
        '''Inherits from class House.'''
        super.__init__(self, self_id)

    def calc_value(self):
        '''Calculates the value of this bugalow.'''
        print('TODO: class House, calc_value')
        # super.value = function


class Mansion(House):
    '''Last of three types of houses.'''

    def __init__(self, self_id):
        '''Inherits from class House.'''
        super.__init__(self, self_id)

    def calc_value(self):
        '''Calculates the value of this mansion.'''
        print('TODO: class House, calc_value')
        # super.value = function


class Water_Element(object):
    '''One of a maximum of four areas desitnated for water.'''

    def __init__(self):
        '''Water is a list of cells on which water is placed.'''
        self.water = []

    def place_water(self, location):
        '''Fills the water list with cells.'''
        self.water.append(location)
