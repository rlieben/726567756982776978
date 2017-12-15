
import sys

from __import__ import *


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
		best_random_map = best_of_random(MAP_20, 19)

		coloured_map(best_random_map['best_map'], 'run_me', 'best')
		plot_data([best_random_map['data']], 'run_me', 'plot')
		save_results(best_random_map['data'], 'run_me', 'data')



	elif command == 2:
		best_greedy = greedy(20, MAP_20)

		coloured_map(best_greedy['best_map'], 'run_me', 'best')
		plot_data([best_greedy['data']], 'run_me', 'plot')
		save_results(best_greedy['data'], 'run_me', 'data')

	elif command == 3:
		hillclimber_map = hillclimber(MAP_20, 1, 20, 1, 0)

		coloured_map(hillclimber_map['best_map'], 'run_me', 'best')
		plot_data([hillclimber_map['data']], 'run_me', 'plot')
		save_results(hillclimber_map['data'], 'run_me', 'data')

	elif command == 4:
		force_move_map = force_move(random_map, 20)

		coloured_map(force_move_map['best_map'], 'run_me', 'best')
		plot_data([force_move_map['data']], 'run_me', 'plot')
		save_results(force_move_map['data'], 'run_me', 'data')

	elif command == 5:
		sa_hillclimber_map = sa_hillclimber(MAP_20, 10, 1, 0, 0.01, 4)

		coloured_map(sa_hillclimber_map['best_map'], 'run_me', 'best')
		plot_data([sa_hillclimber_map['data']], 'run_me', 'plot')
		save_results(sa_hillclimber_map['data'], 'run_me', 'data')
