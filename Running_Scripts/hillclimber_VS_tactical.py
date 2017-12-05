
from __import__ import *

best_random = hillclimber(MAP_20, 10, 10, 1)
print('hillclimber:', best_random.score)

best_hill = tactical_hillclimber(MAP_20, 10, 10, 1)
print('tactical:', best_hill.score)

# scatterplot(best_hill, 'best hill')
