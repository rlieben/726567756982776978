
from __import__ import *

def particle_swarm_map(map_charac):

	out_map = random_generator(map_charac)

	for house in out_map.houses:
		freespace = house.calc_freespace()
		house.direction = {'x' : numpy.uniform(- freespace, freespace),
					 'y' : numpy.uniform(- freespace, freespace)}

		loc = {'x' : house.location['x'] + house.direction['x'],
			   'y' : house.location['y'] + house.direction['y']}
