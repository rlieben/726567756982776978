
from __import__ import *

def particle_swarm_map(map_charac):

	out_map = random_generator(map_charac)
	directions = []

	for house in out_map.houses:
		freespace = house.calc_freespace()
		direction = {'x' : numpy.uniform(- freespace, freespace),
					 'y' : numpy.uniform(- freespace, freespace}

		house.location = {'x' : house.location['x'] + direction['x'],
						  'y' : house.location['y'] + direction['y']}

		directions.append(direction)
