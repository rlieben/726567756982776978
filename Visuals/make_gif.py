import sys
import os
import imageio
#
# import matplotlib as mpl
# import matplotlib.pyplot as plot
# import matplotlib.patches as patches
# import sys
#
# def coloured_map(ah_map, directory, name):
#
# 	out_plot = plot.figure()
# 	ax = out_plot.add_subplot(111)
#
# 	p = []
#
# 	for house in ah_map.houses:
#
# 		p.append(patches.Rectangle((house.corners['lo']['x'],
# 									house.corners['lo']['y']),
# 									house.width, house.height,
# 									facecolor=house.colour))
#
# 	for water in ah_map.water:
#
# 		p.append(patches.Rectangle((water.corners['lo']['x'],
# 									water.corners['lo']['y']),
# 									water.width, water.height,
# 									facecolor='blue'))
#
#
# 	for patch in p:
# 	    ax.add_patch(patch)
#
# 	axes = plot.gca()
# 	ax.set_facecolor('green')
# 	axes.set_xlim([0, ah_map.width])
# 	axes.set_ylim([0, ah_map.height])
#
# 	# out_plot.savefig(name)
#
# 	split = sys.path[1][2]
# 	list_dir = sys.path[0].split(split)
# 	string = ''
# 	for i in range(len(list_dir) - 1):
# 		string += list_dir[i]
# 		string += split
#
# 	out_plot.savefig(string + 'Results' + split + directory + split + name
# 					 + '.png')
#
# 	out_plot.clf()



def make_gif(steps, directory, name):

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
