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

ONE_FAM = {'width' : 8, 'height': 8, 'start_value' : 285000, 'perc' : 0.02,
           'min_free' : 2, 'type' : 'one_family'}

BUNGALOW = {'width' : 10, 'height' : 7.5, 'start_value' : 399000, 'perc' : 0.04,
            'min_free' : 3, 'type' : 'bungalow'}

MANSION = {'width' : 11, 'height' : 10.5, 'start_value' : 610000, 'perc' : 0.06,
           'min_free' : 6, 'type' : 'mansion'}


'''The characteristics of the map.
   Water prev is the minimal percentage of the surface that should be water.
   Nr houses is a list with all number of houses that are allowed.
   Distr houses is the distribution of the different types of houses listed
   above [ONE_FAMILY, BUNGALOW, MANSION]'''

       'nr_houses' : [20, 40, 60], 'distr_houses' : [0.60, 0.25, 0.15]}
