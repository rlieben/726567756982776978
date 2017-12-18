# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


import matplotlib as mpl
import matplotlib.pyplot as plot
import matplotlib.patches as patches


def coloured_map(in_map, directory, name):
	'''Creates a coloured map in given directory.

	Input arguments:
	in_map -- object, input map
	directory -- string, name of directory in results
	name -- string, name of outputfile
	'''

	# init plot
	out_plot = plot.figure()

	# add subplot for rects to be placed on
	ax = out_plot.add_subplot(111)

	# init list of rects to plot
	p = []

	# for every house, add a rect to the list
	for house in in_map.houses:

		p.append(patches.Rectangle((house.corners['lo']['x'],
									house.corners['lo']['y']),
									house.width, house.height,
									facecolor=house.colour))

	# for every water element, add a rect to the list
	for water in in_map.water:

		p.append(patches.Rectangle((water.corners['lo']['x'],
									water.corners['lo']['y']),
									water.width, water.height,
									facecolor='blue'))

	# add patches from list to plot
	for patch in p:
	    ax.add_patch(patch)

	# add axes
	axes = plot.gca()

	# set background colour to green
	ax.set_facecolor('green')

	# set boundries of map
	axes.set_xlim([0, in_map.width])
	axes.set_ylim([0, in_map.height])

	from __import__ import string, split

	# save figure at directory with name
	out_plot.savefig(string + 'Results' + split + directory + split + name
					 + '.png')

	# clear to prevent overwriting and close to prevent overuse of CPU
	out_plot.clf()
	plot.close()
