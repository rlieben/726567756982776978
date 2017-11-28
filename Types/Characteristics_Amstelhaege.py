# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Standard map and houses of the assignment. All measurements are in meters.
'''

'''Three types of homes. '''

ONE_FAM = {'width' : 8, 'height': 8, 'start_value' : 285000, 'perc' : 0.02,
		   'min_free' : 2, 'type' : 'one_family'}

BUNGALOW = {'width' : 10, 'height' : 7.5, 'start_value' : 399000, 'perc' : 0.04,
			'min_free' : 3, 'type' : 'bungalow'}

MANSION = {'width' : 11, 'height' : 10.5, 'start_value' : 610000, 'perc' : 0.06,
		   'min_free' : 6, 'type' : 'mansion'}


'''The characteristics of the map.

Distr houses is the distribution of the different types of houses listed
above [ONE_FAMILY, BUNGALOW, MANSION]
'''

MAP = {'width' : 180, 'height': 160, 'water_prev' : 0.20,
		  'nr_houses' : [20, 40, 60], 'distr_houses' : [0.60, 0.25, 0.15]}

MAP_20 = {'width' : 180, 'height': 160, 'water_prev' : 0.20,
		  'nr_houses' : 20, 'distr_houses' : [0.60, 0.25, 0.15]}

MAP_40 = {'width' : 180, 'height': 160, 'water_prev' : 0.20,
		  'nr_houses' : 40, 'distr_houses' : [0.60, 0.25, 0.15]}

MAP_60 = {'width' : 180, 'height': 160, 'water_prev' : 0.20,
		  'nr_houses' : 60, 'distr_houses' : [0.60, 0.25, 0.15]}
