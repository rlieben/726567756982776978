#!/usr/bin/python

import matplotlib as mpl
import matplotlib.pyplot as plot
import numpy as np

from test_placement import *

# make values from -5 to 5, for this
'''Uiteindelijk moet bij zvals de list worden ingeladen met de waardes die zijn uitgerekend'''
zvals = np.random.rand(100,100)*10-5

print(zvals)

z_vals = ah_map

cell_int = 0

for line in z_vals.grid:
    for cell in line:
        if cell.type == "house":
            cell_int = 1
            print(cell_int)
        else:
            cell_int = 0

print(z_vals)

# make a color map of fixed colors
cmap = mpl.colors.ListedColormap(['red','black','white'])
bounds=[-6,-2,2,6]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# tell imshow about color map so that only set colors are used
img = plot.imshow(cell_int,interpolation='nearest',
                    cmap = cmap, norm=norm)

# make a color bar
plot.colorbar(img,cmap=cmap,
                norm=norm,boundaries=bounds,ticks=[-5,0,5])

plot.show()
