
import sys

from Classes.house import *
from Classes.map import *
from Classes.water import *
from Specifications.amstelhaege import *
from Algorithms.helpers import *
from Algorithms.best_of_random import *
from Algorithms.hillclimber import *
from Algorithms.depthfirst import *
from Visualisations.coloured_map import *
from Visualisations.txtwriter import *
from Visualisations.make_gif import *

while True:
    try:
        command = int(input("Please enter algorithm: "))

    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

if  command > 5:
    print('Give valid algorithm')
else:
    if command == 1:
        best_random_map = best_of_random(MAP_20, 19, True)
        # coloured_map(best_random_map['best_map'], 'best_of_random', 'best')
        # save_results(best_random_map['data'], 'best_of_random', 'data')
        # make_gif(best_random_map['steps'], 'best_of_random', 'random')

    elif command == 2:
        best_depthfirst = depthfirstwater(20, 4, MAP_20)

    elif command == 3:
        hillclimber_map = hillclimber(MAP_20, 1, 20, 1, 0, True)

    elif command == 4:
        particle_map = particle_swarm(random_map, 20, True)

    elif command == 5:
        print('foo')
