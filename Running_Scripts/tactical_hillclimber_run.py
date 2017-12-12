
from __import__ import *

best_hill = hillclimber(MAP_20, 5, 5, 1, 1)
print('tactical:', best_hill.score)
save_results(best_hill['data'], "tactical")