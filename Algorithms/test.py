from __import__ import Map, MAP_20, coloured_map

ah_map = Map(MAP_20)

loc = {'x' : 10, 'y' : 10}

ah_map.place_house(0, loc)
ah_map.remove_house(0)

coloured_map(ah_map, '', 'test')
