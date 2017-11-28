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

    def place_house(ah_map, loc, house_id, type_charac):
        '''Places a one family house on location on the map, with a given id.'''

        new_house = House(house_id, type_charac, loc)

        if house_id == 0:
            ah_map.houses.append(new_house)
        else:
            ah_map.calc_freespace(new_house)

            if new_house.freespace < MANSION['min_free']:
                return False
            else:
                ah_map.houses.append(new_house)
            # return ah_map
