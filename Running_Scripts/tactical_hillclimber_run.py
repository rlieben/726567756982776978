
from __import__ import *

best_hill = hillclimber(MAP_20, 5, 2, 1, 1)

print('tactical:', best_hill['map'].score)
save_results(best_hill['data'], "tactical")