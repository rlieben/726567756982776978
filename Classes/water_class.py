# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

class Water_Element(object):
    '''One of a maximum of four areas destinated for water.'''

    def __init__(self, loc):
        '''Water is a list of cells on which water is placed.'''

        self.location = loc
        self.size = ''
