
from __import__ import *

best_random = best_of_random(MAP_60, 10)
print('best random:', best_random.score)

best_hill = hillclimber(MAP_60, 1, 10, 1)
print('hillclimber:', best_hill['map'].score)

# scatterplot(best_random, 'best of random')
scatterplot(best_hill['map'], 'best of hillclimber 50')
save_results(best_hill['data'], 'hillclimber 60')
