
from __import__ import *

def scatterplot(ah_map, name, directory):

	import matplotlib.patches as patches

	out_plot = plot.figure()
	ax = out_plot.add_subplot(111, aspect='equal')

	p = []

	for house in ah_map.houses:

		p.append(patches.Rectangle((house.corners['lb']['x'],
									house.corners['lb']['y']),
									house.width, house.height,
									facecolor=house.colour))

	for water in ah_map.water:

		p.append(patches.Rectangle((water.corners['lb']['x'],
									water.corners['lb']['y']),
									water.width, water.height,
									facecolor='blue'))


	for patch in p:
	    ax.add_patch(patch)

	axes = plot.gca()
	ax.set_facecolor('green')
	axes.set_xlim([0, ah_map.width])
	axes.set_ylim([0, ah_map.height])

	# # out_plot.savefig(name)
    #
	# split = sys.path[1][2]
	# list_dir = sys.path[0].split(split)
	# string = ''
	# for i in range(len(list_dir) - 1):
	# 	string += list_dir[i]
	# 	string += split
    #
	# out_plot.savefig(string + 'Results' + split + directory + split + name)

	out_plot.show()

	out_plot.clf()
	
ah_map = Map(MAP_20)
ah_map.place_water({'x': random.randint(0,160), 'y': random.randint(0,160)}, 1)
allowed = ah_map.place_house({'x' : 50, 'y' : 50}, 1, ah_map.types[0])
print(allowed)
allowed = ah_map.place_house({'x' : 50, 'y' : 40}, 2, ah_map.types[0])
print(allowed)
#
# for house in ah_map.houses:
# 	print(house.freespace)

# # for i in range(10):
# ah_map = random_generator(MAP_60)
# #
# # fireworks(MAP_20)
#
# scatterplot(ah_map, 'test')
