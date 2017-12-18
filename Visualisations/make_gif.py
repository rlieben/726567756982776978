# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

import sys
import os
import imageio


def make_gif(steps, directory, name):
	'''Creates gif of input images in given directory.

	Input arguments:
	steps -- list, input images
	directory -- string, name of directory in results
	name -- string, name of outputfile
	'''

	from __import__ import coloured_map, string, split


	# k = 0
	# for step in steps:
	# 	coloured_map(step, directory + split + 'tmp_gif', name + str(k))
	# 	k += 1

	png_dir = string + 'Results' + split + directory + split + 'tmp_gif'

	images = []

	for subdir, dirs, files in os.walk(png_dir):

	    for in_file in files:
	        file_path = os.path.join(subdir, in_file)

	        if file_path.endswith(".png"):
	            images.append(imageio.imread(file_path))


	imageio.mimsave(string + 'Results' + split + directory + split +
					name + '.gif', images)
