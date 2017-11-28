# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


import matplotlib as mpl
import matplotlib.pyplot as plot
import numpy as np
import matplotlib.patches as patches

import sys
list_dir = sys.path[0].split('\\')
string = ''
for i in range(len(list_dir) - 1):
    string += list_dir[i]
    string += '\\'

sys.path.insert(0, string)

from Classes.house import *
from Classes.map import *
from Classes.water import *


'''
Creates visual and heatmap for the map.
'''


def scatterplot(ah_map):

    data = []

    for i in range(MAP['nr_houses'][0]):


        x = ah_map.houses[i].location['x']
        y = ah_map.houses[i].location['y']

        colors = (0,0,0)
        area = np.pi*1

        data.append([ah_map.houses[i].corners['lb']['x'], ah_map.houses[i].corners['lb']['y']])
        data.append([ah_map.houses[i].corners['lo']['x'], ah_map.houses[i].corners['lo']['y']])
        data.append([ah_map.houses[i].corners['lo']['x'], ah_map.houses[i].corners['lo']['y']])
        data.append([ah_map.houses[i].corners['ro']['x'], ah_map.houses[i].corners['ro']['y']])
        data.append([ah_map.houses[i].corners['ro']['x'], ah_map.houses[i].corners['ro']['y']])
        data.append([ah_map.houses[i].corners['rb']['x'], ah_map.houses[i].corners['rb']['y']])
        data.append([ah_map.houses[i].corners['rb']['x'], ah_map.houses[i].corners['rb']['y']])
        data.append([ah_map.houses[i].corners['lb']['x'], ah_map.houses[i].corners['lb']['y']])

    # print(data)

    axes = plot.gca()
    axes.set_xlim([0,200])
    axes.set_ylim([0,200])

    # for every value in data
    for i in range(0, len(data)-1, 2):
    	# define lists
    	plot_array_x = []
    	plot_array_y = []
    	# append values in pairs to lists
    	plot_array_x.append(data[i][0])
    	plot_array_x.append(data[i+1][0])
    	plot_array_y.append(data[i][1])
    	plot_array_y.append(data[i+1][1])

    	# plot each of these pairs seperately
    	plot.plot(plot_array_x, plot_array_y, 'g')

    plot.savefig('plot_houses')

    return plot.show()
