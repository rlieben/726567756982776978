
from __import__ import *

best_depthfirst = depthfirst(1)
print('best depthfirst:', best_depthfirst['map'].score)

# best_hill = hillclimber(MAP_20, 50, 100, 2)
# print('hillclimber:', best_hill.score)

scatterplot(best_depthfirst)
# scatterplot(best_hill)
