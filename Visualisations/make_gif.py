import sys
import os
import imageio


def make_gif(steps, directory, name):

	from __import__ import coloured_map

	find_forward = sys.path[0].find('/')
	find_backward = sys.path[0].find('\\')

	if find_forward > find_backward:
		split = '/'
	else:
		split = '\\'

	list_dir = sys.path[0].split(split)
	string = ''
	for i in range(len(list_dir) - 1):
	    string += list_dir[i]
	    string += split

	k = 0
	for step in steps:
		coloured_map(step, directory + split + 'tmp_gif', name + str(k))
		k += 1

	png_dir = string + 'Results' + split + directory + split + 'tmp_gif'

	images = []

	for subdir, dirs, files in os.walk(png_dir):

	    for in_file in files:
	        file_path = os.path.join(subdir, in_file)

	        if file_path.endswith(".png"):
	            images.append(imageio.imread(file_path))


	imageio.mimsave(string + 'Results' + split + directory + split +
					name + '.gif', images)