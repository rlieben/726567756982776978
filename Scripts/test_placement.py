# Group:        726567756982776978
# Assignment:   Amstelhaege

'''
First algorithm that places houses, used to test the classes of classes.py.
'''

from classes import *

grid = Map(WIDTH_MAP, HEIGHT_MAP)

# tries to place one house
grid.houses.append(One_Family(0))
# grid.houses[0].add_house(10, 10)
# grid.grid[10][10].type = 'House'
# for line in grid:
#     print(line)
