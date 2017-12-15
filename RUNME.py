
import sys

from __import__ import *
# from Classes.house import *
# from Classes.map import *
# from Classes.water import *
# from Specifications.amstelhaege import *
# from Algorithms.helpers import *
# from Algorithms.best_of_random import *
# from Algorithms.hillclimber import *
# from Algorithms.greedy import *
# from Algorithms.force_move import *
# from Visualisations.coloured_map import *
# from Visualisations.txtwriter import *
# from Visualisations.make_gif import *

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
        best_greedy = greedy(20, MAP_20)

    elif command == 3:
        hillclimber_map = hillclimber(MAP_20, 1, 20, 1, 0, True)

    elif command == 4:
        force_move_map = force_move(random_map, 20, True)

    elif command == 5:
        best_greedy = greedy(20, MAP_20)
