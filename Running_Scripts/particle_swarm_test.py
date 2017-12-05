
from __import__ import *

particle_map = particle_swarm_map(MAP_20, 1)
print('particle:', particle_map['map'].score)

scatterplot(particle_map['map'], 'particle swarm 1')
save_results(particle_map['data'], 'particle swarm 1')
