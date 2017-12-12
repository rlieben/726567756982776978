
from __import__ import *

ah_map = Map(MAP_3)

ah_map.place_house(0, {'x' : 40, 'y' : 30})
ah_map.place_house(0, {'x' : 30, 'y' : 30})
ah_map.place_house(0, {'x' : 50, 'y' : 50})

particle_map = particle_swarm(ah_map, 100)

# for house in particle_map['map'].houses:
# 	house.calc_freespace(ah_map)
	# print(house.type,'freespace:', house.freespace,
	# 	  '\n direction:', house.direction)

scatterplot(ah_map, 'test_new_houses', '')
