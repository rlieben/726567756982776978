# Study:      Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

from classes import *


'''
Creates upperbound and lowerbound for given problem.
'''


# surface variables
surface_area = 160 * 180
surface_water = surface_area / 5
surface_onefamily = 8 * 8
surface_bungalow = 10 * 7.5
surface_maison = 11 * 10.5

# number of houses with 20, 40, 60
nronefamily_20 = 12
nrbungalow_20 = 5
nrmaison_20 = 3

nronefamily_40 = 24
nrbungalow_40 = 10
nrmaison_40 = 6

nronefamily_60 = 36
nrbungalow_60 = 15
nrmaison_60 = 9

# total surface of houses 20, 40, 60
total_surface_1f_20 = nronefamily_20 * surface_onefamily
total_surface_bu_20 = nrbungalow_20 * surface_bungalow
total_surface_ma_20 = nrmaison_20 * surface_maison

total_surface_1f_40 = nronefamily_40 * surface_onefamily
total_surface_bu_40 = nrbungalow_40 * surface_bungalow
total_surface_ma_40 = nrmaison_40 * surface_maison

total_surface_1f_60 = nronefamily_60 * surface_onefamily
total_surface_bu_60 = nrbungalow_60 * surface_bungalow
total_surface_ma_60 = nrmaison_60 * surface_maison

# lower bound 20-houses
lowerbound_20onefamily = nronefamily_20 * VALUE_1F
lowerbound_20bungalow = nrbungalow_20 * VALUE_BU
lowerbound_20maison = nrmaison_20 * VALUE_MA

# lower bound 40-houses
lowerbound_40onefamily = nronefamily_40 * VALUE_1F
lowerbound_40bungalow = nrbungalow_40 * VALUE_BU
lowerbound_40maison = nrmaison_40 * VALUE_MA

# lower bound 60-houses
lowerbound_60onefamily = nronefamily_60 * VALUE_1F
lowerbound_60bungalow = nrbungalow_60 * VALUE_BU
lowerbound_60maison = nrmaison_60 * VALUE_MA


# print lowerbound values
print("lowerbound 20: ", lowerbound_20onefamily + lowerbound_20bungalow +
                        lowerbound_20bungalow)
print("lowerbound 40: ", lowerbound_40onefamily + lowerbound_40bungalow +
                        lowerbound_40bungalow)
print("lowerbound 60: ", lowerbound_60onefamily + lowerbound_60bungalow +
                        lowerbound_60bungalow)

# upperbound

# calc remaining surface 20-houses
rem_surface_20 = surface_area - (surface_water + total_surface_1f_20 +
                                 total_surface_bu_20 + total_surface_ma_20)
rem_surface_40 = surface_area - (surface_water + total_surface_1f_40 +
                                 total_surface_bu_40 + total_surface_ma_40)
rem_surface_60 = surface_area - (surface_water + total_surface_1f_60 +
                                 total_surface_bu_60 + total_surface_ma_60)

# print upperbound values
print("upperbound 20: ", rem_surface_20 * 4 * (0.6 * 610000))
print("upperbound 40: ", rem_surface_40 * 4 * (0.6 * 610000))
print("upperbound 60: ", rem_surface_60 * 4 * (0.6 * 610000))
