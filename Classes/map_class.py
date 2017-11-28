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

    def place_house(self, loc, house_id, type_charac):
        '''Places a one family house on location on the map, with a given id.'''

        new_house = House(house_id, type_charac, loc)

        if house_id == 0:
            self.houses.append(new_house)
        else:
            self.calc_freespace(new_house)

            if new_house.freespace < MANSION['min_free']:
                return False
            else:
                self.houses.append(new_house)


    def calc_freespace_on_map(self, new_house):
        '''Calculating most freespace on map and receives map and movable house
           as input'''

        # initiate possible freespace variable
        poss_freespace = 0

        # initiate x and y variable for optimization
        best_x = new_house.location['x']
        best_y = new_house.location['y']

        # iterate over map width
        for i in range(0, self.charac['width'], 5):

            # iterate over map height
            for j in range(0, self.charac['height'], 5):

                # set x and y location of new house
                new_house.location['x'] = i
                new_house.location['y'] = j

                # store the possible freespace of new location
                self.calc_freespace(new_house)
                tmp = new_house.freespace

                # if new freespace is greater then update
                if (tmp > poss_freespace):

                    # update new poss freespace
                    poss_freespace = tmp

                    # update location of poss freespace
                    best_x = i
                    best_y = j
        return {'x' : best_x, 'y' : best_y}
