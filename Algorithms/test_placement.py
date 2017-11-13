# Group:        726567756982776978
# Assignment:   Amstelhaege

'''
First algorithm that places houses, used to test the classes of classes.py.
'''

WIDTH_MAP = 160
HEIGHT_MAP = 180
WATER_PREVALENCE = 0.20
NR_HOUSES = [20, 40, 60]
DISTR_HOUSES = [0.60, 0.25, 0.15] # [one_family, bungalow, mansion]

import classes.py
import premises.py

grid = Map(WIDTH_MAP, HEIGHT_MAP)

# tries to place one house
grid.houses.append(One_Family(0))
grid.houses[0].add_house(10, 10)
