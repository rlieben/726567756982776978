# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

import sys

from __import__ import *

def run_me():
    '''Runs the case'''

    # get number of houses
    map_input = int(input('Enter number of houses (20, 40 or 60): '))

    # check if correct input is given
    allowed = False

    while allowed == False:
        if map_input == 20:
            allowed = True
        elif map_input == 40:
            allowed = True
        elif map_input == 60:
            allowed = True
        else:
            map_input = int(input('Invalid number of houses, try again: '))
            allowed = False

    # get the algorithm
    alg = input('Enter algorithm of your choice: ')

    # get number of iterations
    num_it = int(input('Enter number of iterations: '))

    #  check if correct input is given
    allowed = False

    while allowed == False:
        if num_it < 0:
            num_it = int(input('No negative integers, try again: '))
        else:
            allowed = True

    def main(alg, num_it, map_specs):

        '''Runs the algorithm of choice.

        Input arguments:
        alg -- algorithm of choice
        num_it -- number of iterations
        map_specs -- type specifications of the case, from file in folder specifications
        '''

        # set map_specs to right specifications
        if map_specs == 20:
            map_specs = MAP_20
        elif map_specs == 40:
            map_specs = MAP_40
        elif map_specs == 60:
            map_specs = MAP_60

        if alg == 'hillclimber':
            print('Running hillclimber...')

            hillclimber_map = hillclimber(map_specs, 1, num_it, 1, 0, False)

            coloured_map(hillclimber_map['best_map'], 'run_me', 'best')
            plot_data([hillclimber_map['data']], 'run_me', 'plot')
            save_results(hillclimber_map['data'], 'run_me', 'data')

        elif alg == 'best of random':
            print('Running best of random...')

            best_random_map = best_of_random(map_specs, num_it)

            coloured_map(best_random_map['best_map'], 'run_me', 'best')
            plot_data([best_random_map['data']], 'run_me', 'plot')
            save_results(best_random_map['data'], 'run_me', 'data')


        elif alg == 'force move':
            print('Running force move...')

            random_map = best_of_random(map_specs, 10)

            force_move_map = force_move(random_map, num_it)

            coloured_map(force_move_map['best_map'], 'run_me', 'best')
            plot_data([force_move_map['data']], 'run_me', 'plot')
            save_results(force_move_map['data'], 'run_me', 'data')

        elif alg == 'greedy':
            print('Running greedy...')

            print(map_specs)
            best_greedy = greedy(num_it, map_specs)

            coloured_map(best_greedy['best_map'], 'run_me', 'best')
            plot_data([best_greedy['data']], 'run_me', 'plot')
            save_results(best_greedy['data'], 'run_me', 'data')


        elif alg == 'simmulated annealing':
            print('Running simulated annealing...')

            sa_hillclimber_map = sa_hillclimber(map_specs, num_it, 1, 0, 0.01, 4)

            coloured_map(sa_hillclimber_map['best_map'], 'run_me', 'best')
            plot_data([sa_hillclimber_map['data']], 'run_me', 'plot')
            save_results(sa_hillclimber_map['data'], 'run_me', 'data')

        else:
            alg = input('Inalid algorithm, try again.\nEnter algorithm of your choice: ')

            allowed = False

            map_input = int(input('Enter number of houses (20, 40 or 60): '))

            while allowed == False:
                if map_input == 20:
                    map_specs = MAP_20
                    allowed = True
                elif map_input == 40:
                    map_specs = MAP_40
                    allowed = True
                elif map_input == 60:
                    map_specs = MAP_60
                    allowed = True
                else:
                    map_input = int(input('Invalid number of houses, try again: '))
                    allowed = False

            num_it = int(input('Number of iterations: '))

            allowed = False

            while allowed == False:
                if num_it < 0:
                    num_it = int(input('No negative integers, try again: '))
                else:
                    allowed = True

            main(alg, num_it, map_input)

    main(alg, num_it, map_input)

run_me()
