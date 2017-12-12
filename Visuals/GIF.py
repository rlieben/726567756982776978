
import sys
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

import os
import imageio

file_name = 'HOI'
# source = 'TESTparticle'
png_dir = string + 'Running_Scripts' + split + 'results'
images = []
for subdir, dirs, files in os.walk(png_dir):
    for in_file in files:
        file_path = os.path.join(subdir, in_file)
        if file_path.endswith(".png"):
            images.append(imageio.imread(file_path))
imageio.mimsave(string + 'Results' + split + file_name + '.gif', images)
