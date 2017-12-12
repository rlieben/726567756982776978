
from __import__ import *

best_hill = sa_hillclimber(MAP_20, 5, 3, 1)

print('tactical:', best_hill['map'].score)
save_results(best_hill['data'], "tactical")
