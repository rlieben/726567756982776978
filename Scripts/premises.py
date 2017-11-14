# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Standard map and houses of the assignment. All measurements are in half meters.
'''


'''Three types of homes.
   Size is the height and width of the house.
   Start value is value of house without extra from free space.
   Perc is the percentage extra value created by every half meter of free space.
   Min free is the minimal length (in half meters) of free space needed.
   Type is a string containing the type of the house.'''

ONE_FAMILY = {'size' : [16, 16], 'start_value' : 285000, 'perc' : 0.015,
              'min_free' : 4, 'type' : 'one_family'}

BUNGALOW = {'size' : [20, 15], 'start_value' : 399000, 'perc' : 0.02,
            'min_free' : 6, 'type' : 'bungalow'}

MANSION = {'size' : [22, 21], 'start_value' : 610000, 'perc' : 0.03,
           'min_free' : 12, 'type' : 'mansion'}


'''The characteristics of the map.
   Water prev is the minimal percentage of the surface that should be water.
   Nr houses is a list with all number of houses that are allowed.
   Distr houses is the distribution of the different types of houses listed
   above [ONE_FAMILY, BUNGALOW, MANSION]'''

MAP = {'width' : 360, 'height': 320, 'water_prev' : 0.20,
       'nr_houses' : [20, 40, 60], 'distr_houses' : [0.60, 0.25, 0.15]}
