# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import sys
list_dir = sys.path[0].split('\\')
string = ''
for i in range(len(list_dir) - 1):
	string += list_dir[i]
	string += '\\'

sys.path.insert(0, string)

import random
from Classes.house import *
from Classes.water import *
from Characteristics.Amstelhaege import *


class Map(object):
	'''List that keeps track of all the houses and water.'''

	def __init__(self, map_charac):
		'''Creates map.

		Input arguments:
		width -- width of the map
		height -- height of the map
		'''

		self.width = map_charac['width']
		self.height = map_charac['height']
		self.water_prev = map_charac['water_prev']
		self.nr_houses = map_charac['nr_houses']
		self.distr_houses = map_charac['distr_houses']
		self.types = map_charac['types_houses']

		self.score = 0
		self.houses = []
		self.water = []


	def place_house(self, loc, house_id, type_charac):
		'''Places a house on the map.

		Input arguments:
		loc -- location where the house needs to be placed
		house_id -- id corresponding to the house being placed
		type_charac -- characteristics of the house being placed
		'''

		new_house = House(house_id, type_charac, loc)

		self.houses.append(new_house)

		for house in self.houses:
			if house.calc_freespace(self) == False:
				del self.houses[len(self.houses) - 1]
				return False
			if house.freespace < house.min_free:
				del self.houses[len(self.houses) - 1]
				return False

		return True

	def place_water(self, loc, water_id):
		'''Places water on the map

		Input arguments:
		loc -- Location where the water body needs to be placed
		water_id -- id corresponding to the water body being placed
		'''

		allowed = False

		while allowed == False:
			x = random.uniform(0, (self.water_prev * self.width * self.height))
			y = (self.water_prev * self.width * self.height) / x

		for water in self.water:
			if water.corners['lb']['x'] < 0 or \
				water.corners['rb']['x'] > self.width or \
				water.corners['lb']['y'] > self.height or \
				water.corners['lo']['y'] < 0:
				allowed = False

		if ((x / y) > 0.25) & ((x / y) < 4):
				allowed = True

		size = {'width': x, 'height': y}

		new_water = Water(loc, water_id, size)

		self.water.append(new_water)


	def calc_freespace_on_map(self, new_house):
		'''Calculating location with the most freespace on map.

		Input arguments:
		new_house --  house that is being moved
		'''

		# initiate possible freespace variable
		poss_freespace = 0

		coordinates = []

		# initiate x and y variable for optimization
		# best_x = new_house.location['x']
		# best_y = new_house.location['y']

		# iterate over map width
		for i in range(5, self.width, 5):

		

			# iterate over map height
			for j in range(5, self.height, 5):

			

				# # set x and y location of new house
				# new_house.location['x'] = i
				# new_house.location['y'] = j

				# print("x coordinate: ", i)
				# print("y coordinate:", j)

				new_house.calc_freespace(self)

				# store the possible freespace of new location
				if (new_house.calc_freespace(self) != False):
					

					tmp = new_house.freespace


					# print("tmp over whole map: ", tmp, "coordinates", i, j)


					# if new freespace is greater then update
					if (tmp >= poss_freespace):

						# update new poss freespace
						poss_freespace = tmp

						# print("tmp: ", tmp)

						# update location of poss freespace
						coordinates.append({'x' : i, 'y' : j})

						# best_x = i
						# best_y = j


		return coordinates


	def random_swap_houses(self, nr_houses):
		'''Moves, every iteration, three houses for optimalization.

		Input arguments:
		in_map -- input map
		'''

		tmp_index = []
		tmp_houses = []

		for i in range(nr_houses):
			tmp_index.append(int(numpy.random.uniform(0, len(self.houses) - 1)))
			tmp_houses.append(self.houses[tmp_index[i]])
			del self.houses[tmp_index[i]

		# add same amount of houses which were deleted
		for i in range(nr_houses):

			allowed = False

			while allowed == False:

				loc = {'x' : random.uniform(0, self.height),
					   'y' : random.uniform(0, self.width)}

				allowed = self.place_house(loc, tmp_houses[i].self_id,
										   self.types[tmp_houses[i].index_nr])


	def tactical_swap_houses(self, nr_houses):
		''' Moves, every iteration, three houses for optimalization.

		Input arguments:
		in_map -- input map
		nr_houses -- nr of houses swapped
		'''

		for i in range(nr_houses):

			tmp_house = self.houses[i]
			del self.houses[i]

			# print("nr of houses i", i, nr_houses)


			print("index tactical swap:", i)
			allowed = False

			ctr = 0

			coordinates = self.calc_freespace_on_map(tmp_house)

			# print (len(coordinates))
			# print coordinates
			j = len(coordinates) - 1

			while (allowed == False):
				
				allowed = self.place_house(coordinates[j], tmp_house.self_id,
											   self.types[tmp_house.index_nr])

				j += -1

				

			self.place_house(coordinates[j], tmp_house.self_id,
									   self.types[tmp_house.index_nr])

			print("allowed status voor place:", allowed)
					# print(" ")
					# print("locations: ", coordinates)

					

					# print(" j ")
					# print(coordinates[-j])

					
					# print("allowed na place:", allowed)
					# print("counter of allowed statement :", ctr)
			ctr += 1


	def calc_score(self):
		'''Calculates score of map.

		Input arguments:
		ah_map -- created map
		'''

		summy = 0
		for house in self.houses:
			house.calc_freespace(self)
			house.calc_value()
			summy += house.value

		self.score = summy
		return summy
