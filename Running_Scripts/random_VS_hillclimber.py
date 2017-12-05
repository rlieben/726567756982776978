
from __import__ import *

best_random = best_of_random(MAP_20, 1)
print('best random:', best_random.score)

# best_hill = hillclimber(MAP_20, 10, 10, 2)
# print('hillclimber:', best_hill.score)

scatterplot(best_random, 'best of random')
# scatterplot(best_hill)
