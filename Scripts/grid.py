# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


import matplotlib as mpl
import matplotlib.pyplot as plot
import numpy as np

from random_generator import *


'''
Creates visual and heatmap for the map.
'''

def grid_houses():
    # values indicating what ind of house is implemented
    z_vals = create_test()

    # create new grid where values are stored
    int_grid = [[0 for x in range(MAP['height'])] for y in range(MAP['width'])]

    # change values into integers
    for i in range(MAP['width']):
        for j in range(MAP['height']):
            if z_vals.grid[i][j].type == 'one_family':
                int_grid[i][j] = int(1)
            if z_vals.grid[i][j].type == 'bungalow':
                int_grid[i][j] = int(2)
            if z_vals.grid[i][j].type == 'mansion':
                int_grid[i][j] = int(3)
            if z_vals.grid[i][j].type == 'water':
                int_grid[i][j] = int(4)
            if z_vals.grid[i][j].type == 'empty':
                int_grid[i][j] = int(0)

    # make a color map of fixed colors
    cmap = mpl.colors.ListedColormap(['green','red','black','white','blue'])
    bounds=[0,1,1,2,2,3,4,5]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    # tell imshow about color map so that only set colors are used
    img = plot.imshow(int_grid,interpolation='nearest',
                        cmap = cmap, norm=norm)

    # make a color bar
    plot.colorbar(img,cmap=cmap,
                    norm=norm,boundaries=bounds,ticks=[0,1,2,3,4,5])

    # score = calc_score(z_vals)
    # print(score)

    return plot.show()

grid_houses()
