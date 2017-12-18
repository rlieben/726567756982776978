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

	# init name
	k = 0

	# create coloured map for every step of list
	for step in steps:
		coloured_map(step, directory + split + 'tmp_gif', str(k).zfill(3))
		k += 1

	# create directory to extract pngs
	png_dir = string + 'Results' + split + directory + split + 'tmp_gif'

	# init list for images to turn into gif
	images = []

	# first add file path to subdirectory, then add pngs to list of images
	for subdir, dirs, files in os.walk(png_dir):

	    for in_file in files:
	        file_path = os.path.join(subdir, in_file)

	        if file_path.endswith(".png"):
	            images.append(imageio.imread(file_path))

	# turn images into gif and save in directory with name
	imageio.mimsave(string + 'Results' + split + directory + split +
					name + '.gif', images)
