
def depthfirst(runs):
	''' Places house random and searches for the best child.

	Input arguments:
	runs -- integer, how many runs of the function

	Returns:
	ah_map -- best map with 20 houses
	score -- score of best map
	'''

	# initializes map
	ah_map = Map(MAP_20)

	# initialize score variables
	tempscore = 0
	score = 0

	# amount of runs for script
	for run in range(runs):







		# calc score of created map

		tmpscore  = ah_map.calc_score()



		# update best score if greater
		if tmpscore > score:

			score = tmpscore

	# returns created map and score
