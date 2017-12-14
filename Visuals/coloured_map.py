

def coloured_map(ah_map, name, directory):

	import matplotlib.patches as patches

	out_plot = plot.figure()
	ax = out_plot.add_subplot(111)

	p = []

	for house in ah_map.houses:

		p.append(patches.Rectangle((house.corners['lo']['x'],
									house.corners['lo']['y']),
									house.width, house.height,
									facecolor=house.colour))

	for water in ah_map.water:

		p.append(patches.Rectangle((water.corners['lo']['x'],
									water.corners['lo']['y']),
									water.width, water.height,
									facecolor='blue'))


	for patch in p:
	    ax.add_patch(patch)

	axes = plot.gca()
	ax.set_facecolor('green')
	axes.set_xlim([0, ah_map.width])
	axes.set_ylim([0, ah_map.height])

	# out_plot.savefig(name)

	split = sys.path[1][2]
	list_dir = sys.path[0].split(split)
	string = ''
	for i in range(len(list_dir) - 1):
		string += list_dir[i]
		string += split

	out_plot.savefig(string + 'Results' + split + directory + split + name)

	out_plot.clf()

	# return out_plot.show()
