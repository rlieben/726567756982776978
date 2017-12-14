
from __import__ import *

ah_map = random_generator(MAP_20)

while len(ah_map.water) < 4:
    ah_map.place_water(1,4)

scatterplot(ah_map, 'test')

# max_freespace = 0
#
# d_house = House(100,MAP_20['types_houses'][0], None)
#
# ah_map.construction.append(d_house)
#
# # get location with max freespace
# fpm = ah_map.calc_freespace_on_map()
#
# best_loc = fpm[0][-1]
#
#
# bx = []
# sx = []
# by = []
# sy = []
#
# for house in ah_map.houses:
#         if house.corners['lb']['x'] > best_loc['x']:
#             bx.append(house)
#         if house.corners['rb']['x'] < best_loc['x']:
#             sx.append(house)
#         if house.corners['lb']['y'] > best_loc['y']:
#             by.append(house)
#         if house.corners['lo']['y'] < best_loc['y']:
#             sy.append(house)
#
# for house in bx:
#     verhouding = 0
#     bx_diff = float('inf')
#     x_diff = house.location['x'] - best_loc['x']
#     y_diff = abs(house.location['y'] - best_loc['y'])
#     new_verhouding = x_diff / y_diff
#     new_diff = house.corners['lb']['x'] - best_loc['x']
#     if new_diff < bx_diff and new_verhouding > verhouding:
#         bx_diff = new_diff
#
# for house in sx:
#     verhouding = 0
#     sx_diff = float('inf')
#     x_diff = best_loc['x'] - house.location['x']
#     y_diff = abs(house.location['y'] - best_loc['y'])
#     new_verhouding = x_diff / y_diff
#     new_diff = best_loc['x'] - house.corners['lb']['x']
#     if new_diff < sx_diff and new_verhouding > verhouding:
#         sx_diff = new_diff
#
# for house in by:
#     verhouding = 0
#     by_diff = float('inf')
#     x_diff = abs(house.location['x'] - best_loc['x'])
#     y_diff = house.location['y'] - best_loc['y']
#     new_verhouding = x_diff / y_diff
#     new_diff = house.corners['lb']['y'] - best_loc['y']
#     if new_diff < by_diff and new_verhouding > verhouding:
#         by_diff = new_diff
#
# for house in sy:
#     verhouding = 0
#     sy_diff = float('inf')
#     x_diff = abs(house.location['x'] - best_loc['x'])
#     y_diff = best_loc['y'] - house.location['y']
#     new_verhouding = x_diff / y_diff
#     print(new_verhouding)
#     new_diff = best_loc['y'] - house.corners['lb']['y']
#     if new_diff < sy_diff and new_verhouding > verhouding:
#         sy_diff = new_diff
#
#
# freespace_len = fpm[1][-1]
# j = len(fpm[1])
# del ah_map.construction[0]
#
#
# for i in range(4):
#
#     j = (j - 1) - i
#
#     freespace_len = fpm[1][j]
#
#     width = freespace_len * 2
#     height = freespace_len * 2
#
#     size = {'width': width, 'height': height}
#
#     print(size, best_loc)
#
#     ah_map.water.append(Water(100, size, best_loc))
