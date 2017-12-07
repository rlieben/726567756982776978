
from __import__ import *

ah_map = Map(MAP_20)
ah_map.place_water({'x': random.randint(0,160), 'y': random.randint(0,160)}, 1)
# allowed = ah_map.place_house({'x' : 50, 'y' : 50}, 1, ah_map.types[0])
# print(allowed)
# allowed = ah_map.place_house({'x' : 50, 'y' : 40}, 2, ah_map.types[0])
# print(allowed)
#
# for house in ah_map.houses:
# 	print(house.freespace)

# ah_map = random_generator(MAP_20)
#
# fireworks(MAP_20)

scatterplot(ah_map, 'test')
