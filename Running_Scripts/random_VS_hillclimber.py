
from __import__ import *

# best_random = best_of_random(MAP_20, 100)
# print('best random:', best_random.score)

best_hill = hillclimber(MAP_20, 1, 100, 1)
print('hillclimber:', best_hill['map'].score)

# scatterplot(best_random, 'best of random')
scatterplot(best_hill['map'], 'best of hillclimber 20')
save_results(best_hill['data'], 'hillclimber')
