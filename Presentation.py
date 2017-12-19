from __import__ import *


num_it = 100
map_specs = MAP_20
in_map = random_generator(map_specs)



hillclimber_map = hillclimber(in_map, num_it, 1, 0, False)
force_move_map = force_move(in_map, num_it, False)
# sa_hillclimber_map = sa_hillclimber(in_map, 1, 0, 0.01, 4, False)
hillclimber_map_heuristic = hillclimber(in_map, num_it, 1, 1, False)

# best_random_map = best_of_random(map_specs, num_it, False)
# best_greedy = greedy(num_it, map_specs, 5, False)


plot_data([force_move_map['data'], hillclimber_map['data'], hillclimber_map_heuristic['data']], 'presentation', 'plot_rand_in_map')
# plot_data([best_greedy['data'], best_of_random_map['data']], 'presentation', 'plot_best_rand_greedy')

# coloured_map(sa_hillclimber_map['best_map'], 'presentation', 'best_sa')
coloured_map(force_move_map['best_map'], 'presentation', 'best_force_move')
coloured_map(hillclimber_map['best_map'], 'presentation', 'best_hillclimber')
coloured_map(hillclimber_map_heuristic['best_map'], 'presentation', 'best_hillclimber_heuristic')
# coloured_map(best_greedy['best_map'], 'presentation', 'best_greedy')
# coloured_map(best_random_map['best_map'], 'presentation', 'best_of_random')


# save_results(sa_hillclimber_map['data'], 'presentation', 'data_sa')
save_results(force_move_map['data'], 'presentation', 'data_force')
save_results(hillclimber_map['data'], 'presentation', 'data_hillclimber')
save_results(hillclimber_map_heuristic['data'], 'presentation', 'data_hillclimber_heur')
# save_results(best_greedy['best_map'], 'presentation', 'data_greedy')
# save_results(best_random_map['best_map'], 'presentation', 'data_best_random')
