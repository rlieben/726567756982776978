
from __import__ import *

random_map = best_of_random(MAP_40, 1)
particle_map = particle_swarm(random_map, 10)
print('particle:', particle_map['map'].score)

# scatterplot(particle_map['map'], 'particle swarm 1', '')
save_results(particle_map['data'], 'particle swarm 1')
