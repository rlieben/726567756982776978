#!/usr/bin/python

import matplotlib as mpl
import matplotlib.pyplot as plot
import numpy as np

from test_placement import *
# from classes import *

# make values from -5 to 5, for this
'''Uiteindelijk moet bij zvals de list worden ingeladen met de waardes die zijn uitgerekend'''

# values indicating what ind of house is implemented
z_vals = create_test()

# create new grid where values are stored
int_grid = [[0 for x in range(HEIGHT_MAP)] for y in range(WIDTH_MAP)]

# change values into integers
for i in range(WIDTH_MAP):
    for j in range(HEIGHT_MAP):
        if z_vals.grid[i][j].type == "house":
            int_grid[i][j] = int(1)
        if z_vals.grid[i][j].type == 'one_family':
            int_grid[i][j] = int(2)
        if z_vals.grid[i][j].type == 'bungalow':
            int_grid[i][j] = int(3)
        if z_vals.grid[i][j].type == 'mansion':
            int_grid[i][j] = int(4)
        if z_vals.grid[i][j].type == 'water':
            int_grid[i][j] = int(5)
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

plot.show()
