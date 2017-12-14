# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


'''
Standard map and houses of the assignment. All measurements are in meters.
'''

'''Three types of homes. '''

HOUSES_LIST = [ {'type' : 'one_family', 'index' : 0, 'width' : 8, 'height': 8,
				 'start_value' : 285000, 'perc' : 0.02, 'min_free' : 2,
				 'colour' : 'yellow'},
				{'type' : 'bungalow', 'index' : 1, 'width' : 10, 'height' : 7.5,
			 	 'start_value' : 399000, 'perc' : 0.04, 'min_free' : 3,
				 'colour' : 'orange'},
				{'type' : 'mansion', 'index' : 2, 'width' : 11, 'height' : 10.5,
				 'start_value' : 610000, 'perc' : 0.06, 'min_free' : 6,
				 'colour' : 'red'}]


'''The characteristics of the map.

Distr houses is the distribution of the different types of houses listed
above [ONE_FAMILY, BUNGALOW, MANSION]
'''

MAP_3 = {'width' : 180, 'height': 160, 'water_prev' : 0.20,
		  'nr_houses' : 3, 'distr_houses' : [1, 0, 0],
		  'types_houses' : HOUSES_LIST}

MAP_20 = {'width' : 180, 'height': 160, 'water_prev' : 0.20,
		  'nr_houses' : 20, 'distr_houses' : [0.60, 0.25, 0.15],
		  'types_houses' : HOUSES_LIST}

MAP_40 = {'width' : 180, 'height': 160, 'water_prev' : 0.20,
		  'nr_houses' : 40, 'distr_houses' : [0.60, 0.25, 0.15],
		  'types_houses' : HOUSES_LIST}

MAP_60 = {'width' : 180, 'height': 160, 'water_prev' : 0.20,
		  'nr_houses' : 60, 'distr_houses' : [0.60, 0.25, 0.15],
		  'types_houses' : HOUSES_LIST}
