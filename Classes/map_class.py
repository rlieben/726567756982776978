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

from Classes.house_class import *
# from Classes.map_class import *
from Classes.water_class import *
from Types.Characteristics_Amstelhaege import *
# from Algorithms.algorithms import *


class Map(object):
	'''List that keeps track of all the houses and water.'''

	def __init__(self, width, height):
		'''Creates map.

		Input arguments:
		width -- width of the map
		height -- height of the map
		'''

		self.houses = []
		self.water = []
		self.charac = {'width' : width, 'height' : height}


	def place_house(self, loc, house_id, type_charac):
		'''Places a house on the map.

		Input arguments:
		loc -- location where the house needs to be placed
		house_id -- id corresponding to the house being placed
		type_charac -- characteristics of the house being placed
		'''

		new_house = House(house_id, type_charac, loc)

		if house_id == 0:
			self.houses.append(new_house)
		else:
			self.calc_freespace(new_house)

			if new_house.freespace < MANSION['min_free']:
				return False
			else:
				self.houses.append(new_house)


	def calc_freespace_on_map(self, new_house):
		'''Calculating location with the most freespace on map.

		Input arguments:
		new_house --  house that is being moved
		'''

		# initiate possible freespace variable
		poss_freespace = 0

		# initiate x and y variable for optimization
		best_x = new_house.location['x']
		best_y = new_house.location['y']

		# iterate over map width
		for i in range(0, self.charac['width'], 5):

			# iterate over map height
			for j in range(0, self.charac['height'], 5):

				# set x and y location of new house
				new_house.location['x'] = i
				new_house.location['y'] = j

				# store the possible freespace of new location
				self.calc_freespace(new_house)
				tmp = new_house.freespace

				# if new freespace is greater then update
				if (tmp > poss_freespace):

					# update new poss freespace
					poss_freespace = tmp

					# update location of poss freespace
					best_x = i
					best_y = j
		return {'x' : best_x, 'y' : best_y}
