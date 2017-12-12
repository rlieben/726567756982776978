
from __import__ import *

ah_map = Map(MAP_3)

ah_map.place_house(0, {'x' : 97, 'y' : 149})
ah_map.place_house(0, {'x' : 100, 'y' : 155})
# ah_map.place_house(0, {'x' : 50, 'y' : 50})

# particle_map = particle_swarm(ah_map, 100)

for house in ah_map.houses:
	house.calc_freespace(ah_map)
	print(house.type,'freespace:', house.freespace,
		  '\n direction:', house.direction)

scatterplot(ah_map, 'test_new_houses')
