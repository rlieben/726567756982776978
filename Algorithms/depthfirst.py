from __import__ import *

def scatterplot(ah_map, name):

	data = []

	for i in range(len(ah_map.houses)):


		x = ah_map.houses[i].location['x']
		y = ah_map.houses[i].location['y']

		colors = (0, 0, 0)
		area = np.pi * 1

		data.append([ah_map.houses[i].corners['lb']['x'],
					 ah_map.houses[i].corners['lb']['y']])
		data.append([ah_map.houses[i].corners['lo']['x'],
					 ah_map.houses[i].corners['lo']['y']])
		data.append([ah_map.houses[i].corners['lo']['x'],
					 ah_map.houses[i].corners['lo']['y']])
		data.append([ah_map.houses[i].corners['ro']['x'],
					 ah_map.houses[i].corners['ro']['y']])
		data.append([ah_map.houses[i].corners['ro']['x'],
					 ah_map.houses[i].corners['ro']['y']])
		data.append([ah_map.houses[i].corners['rb']['x'],
					 ah_map.houses[i].corners['rb']['y']])
		data.append([ah_map.houses[i].corners['rb']['x'],
					 ah_map.houses[i].corners['rb']['y']])
		data.append([ah_map.houses[i].corners['lb']['x'],
					 ah_map.houses[i].corners['lb']['y']])

	for i in range(len(ah_map.water)):
		data.append([ah_map.water[i].corners['lb']['x'],
					 ah_map.water[i].corners['lb']['y']])
		data.append([ah_map.water[i].corners['lo']['x'],
					 ah_map.water[i].corners['lo']['y']])
		data.append([ah_map.water[i].corners['lo']['x'],
					 ah_map.water[i].corners['lo']['y']])
		data.append([ah_map.water[i].corners['ro']['x'],
					 ah_map.water[i].corners['ro']['y']])
		data.append([ah_map.water[i].corners['ro']['x'],
					 ah_map.water[i].corners['ro']['y']])
		data.append([ah_map.water[i].corners['rb']['x'],
					 ah_map.water[i].corners['rb']['y']])
		data.append([ah_map.water[i].corners['rb']['x'],
					 ah_map.water[i].corners['rb']['y']])
		data.append([ah_map.water[i].corners['lb']['x'],
					 ah_map.water[i].corners['lb']['y']])

	axes = plot.gca()
	axes.set_xlim([0, ah_map.width])
	axes.set_ylim([0, ah_map.height])

	# for every value in data
	for i in range(0, len(data) - 1, 2):
		# define lists
		plot_array_x = []
		plot_array_y = []

		# append values in pairs to lists
		plot_array_x.append(data[i][0])
		plot_array_x.append(data[i + 1][0])
		plot_array_y.append(data[i][1])
		plot_array_y.append(data[i + 1][1])

		# plot each of these pairs seperately
		plot.plot(plot_array_x, plot_array_y, 'g')

	plot.savefig(name)

	plot.clf()

	# split = sys.path[1][2]
	# list_dir = sys.path[0].split(split)
	# string = ''
	# for i in range(len(list_dir) - 1):
	# 	string += list_dir[i]
	# 	string += split
    #
	# plot.savefig(string +  'Results' + split + name)

	# return plot.show()

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

		# iterates over houses
		for i in range(len(ah_map.construction)):


			print("test", len(ah_map.construction))

			# sets house id
			# house_id = 100 * (int(j) + 1) + i

			allowed = False

			# get freespace coordinates on map
			coordinates = ah_map.calc_freespace_on_map()

			j = len(coordinates) - 1

			# place house where valid beginning with biggest freespace to smallest
			while (allowed == False):

				allowed = ah_map.place_house(0, coordinates[j])

				j += -1

			scatterplot(ah_map, "depthfirst" + str(i))



		# calc score of created map

		tmpscore  = ah_map.calc_score()



		# update best score if greater
		if tmpscore > score:

			score = tmpscore

	# returns created map and score
	return {'map': ah_map, 'score' : score}
