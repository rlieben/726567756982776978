# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


import matplotlib as mpl
import matplotlib.pyplot as plot
import numpy as np

from algorithms import *


'''
Creates visual and heatmap for the map.
'''


def scatterplot(ah_map):

    for i in range(MAP['nr_houses'][0]):

        x = ah_map.houses[i].location['x']
        y = ah_map.houses[i].location['y']

        colors = (0,0,0)
        area = np.pi*3
        # ax.annotate(data.houses[i].house_id, (x,y))
        plot.scatter(x, y, s=area, c=colors, alpha=0.5)

        # draw lines to corners
        plot.plot(ah_map.houses[i].corners)

    plot.title('scatterplot for houses')
    plot.xlabel('x (m)')
    plot.ylabel('y (m)')

    return plot.show()
