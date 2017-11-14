# Group:        726567756982776978
# Assignment:   Amstelhaege

'''
First algorithm that places houses, used to test the classes of classes.py.
'''

from classes import *

grid = Map(WIDTH_MAP, HEIGHT_MAP)

x_loc = 0
y_loc = 0

# tries to place one house
grid.houses.append(One_Family(0))
grid.houses[0].add_structure(x_loc, y_loc)
grid.grid[x_loc][y_loc].type = 'House'
# for line in grid.grid:
#     print(line)
