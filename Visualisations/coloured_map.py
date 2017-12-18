# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

import matplotlib as mpl
import matplotlib.pyplot as plot
import matplotlib.patches as patches
import sys

def coloured_map(in_map, directory, name):
	'''Creates a coloured map in given directory.

	Input arguments:
	in_map -- object, input map
	directory -- string, name of directory in results
	name -- string, name of outputfile
	'''

	out_plot = plot.figure()
	ax = out_plot.add_subplot(111)

	p = []

	for house in in_map.houses:

		p.append(patches.Rectangle((house.corners['lo']['x'],
									house.corners['lo']['y']),
									house.width, house.height,
									facecolor=house.colour))

	for water in in_map.water:

		p.append(patches.Rectangle((water.corners['lo']['x'],
									water.corners['lo']['y']),
									water.width, water.height,
									facecolor='blue'))


	for patch in p:
	    ax.add_patch(patch)

	axes = plot.gca()
	ax.set_facecolor('green')
	axes.set_xlim([0, in_map.width])
	axes.set_ylim([0, in_map.height])

	from __import__ import string, split


	out_plot.savefig(string + 'Results' + split + directory + split + name
					 + '.png')

	out_plot.clf()
	plot.close()
