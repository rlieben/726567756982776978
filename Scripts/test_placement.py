# Group:        726567756982776978
# Assignment:   Amstelhaege

'''
First algorithm that places houses, used to test the classes of classes.py.
'''

from classes import *

grid = Map(WIDTH_MAP, HEIGHT_MAP)

x_loc = 5
y_loc = 5

# tries to place one house
grid.houses.append(One_Family(0))

for i in range(x_loc, x_loc + SIZE_1F[0]):
    for j in range(y_loc, y_loc + SIZE_1F[1])
        grid.houses[0].add_structure(i, j)

for line in grid.houses[0]:
    for cell in line:
        grid.grid[cell[0], cell[1]]

for line in grid.grid:
    print(line)
