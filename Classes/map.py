# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import copy
import numpy

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
		self.construction = self.create_construction(map_charac)

		self.score = None
		self.houses = []
		self.water = []


	def create_construction(self, map_charac):

		from __import__ import House

		house_id = 0
		loc = {'x' : None, 'y' : None}
		construction = []

		for i in range(len(map_charac['distr_houses'])):
			for j in range(int(map_charac['distr_houses'][i]
						   	   * map_charac['nr_houses'])):

				construction.append(House(house_id,
										  map_charac['types_houses'][i], loc))
				house_id += 1

		return construction


	def rand_loc_water(self):
		'''generates random location'''

		loc = {'x' : random.uniform((0 + 0.5 * water.width), \
				  	(MAP_20['width'] - 0.5 * water.width)), \
			   'y' : random.uniform((0 + 0.5 * water.height), \
		  			(MAP_20['height'] - 0.5 * water.height))}

		return loc


	def place_house(self, index, loc):

		# copy the house to be placed
		tmp_house = copy.copy(self.construction[index])

		# add the new location to this copy and update its corners
		tmp_house.location = loc
		tmp_house.find_corners()

		# check out of bounds map
		for c in tmp_house.corners:

				if (tmp_house.corners[c]['x'] > self.width or
					tmp_house.corners[c]['x'] < 0 or
					tmp_house.corners[c]['y'] > self.height or
					tmp_house.corners[c]['y']  < 0):

					# stop function if house if out of bounds
					return False

        # check for overlap water
		for water in self.water:

			for c in tmp_house.corners:

				if (tmp_house.corners[c]['x'] >= water.corners['lb']['x'] and
					tmp_house.corners[c]['x'] <= water.corners['rb']['x'] and
				    tmp_house.corners[c]['y'] <= water.corners['lb']['y'] and
				    tmp_house.corners[c]['y'] >= water.corners['lo']['y']):

					# stop function if there is overlap
					return False


		# check for overlap other house
		for house in self.houses:

			# check if location falls between walls
			if (tmp_house.location['x'] > house.corners['lb']['x'] and
				tmp_house.location['x'] < house.corners['rb']['x'] and
				tmp_house.location['y'] > house.corners['lo']['y'] and
				tmp_house.location['y'] < house.corners['lb']['y']):
				return False

			# check for every corner if it's not in a other house
			for c in tmp_house.corners:

				if (tmp_house.corners[c]['x'] >= house.corners['lb']['x'] and
					tmp_house.corners[c]['x'] <= house.corners['rb']['x'] and
				    tmp_house.corners[c]['y'] <= house.corners['lb']['y'] and
				    tmp_house.corners[c]['y'] >= house.corners['lo']['y']):

					# stop function if there is overlap
					return False

			# check for every corner of other house if it's not in this house
			for c in house.corners:

				if (house.corners[c]['x'] >= tmp_house.corners['lb']['x'] and
					house.corners[c]['x'] <= tmp_house.corners['rb']['x'] and
				    house.corners[c]['y'] <= tmp_house.corners['lb']['y'] and
				    house.corners[c]['y'] >= tmp_house.corners['lo']['y']):

					# stop function if there is overlap
					return False

		# add copy to list of houses to check freespace
		self.houses.append(tmp_house)

		# check if new house does not violate minimal freespace of houses
		for house in self.houses:

			house.calc_freespace(self)
			if house.freespace < house.min_free:

				# if freespace is violated, delete house from list and stop
				del self.houses[len(self.houses) - 1]
				return False

		# remove original from construction list
		del self.construction[index]

		# return True for verification
		return True



	def remove_house(self, index):

		tmp_house = copy.copy(self.houses[index])

		tmp_house.location = {'x' : None, 'y' : None}
		tmp_house.freespace = None
		tmp_house.value = None

		self.construction.append(tmp_house)
		del self.houses[index]


	def place_water_random(self, nr_water, index, loc):
		'''Places water on the map

		Input arguments:
		loc -- Location where the water body needs to be placed
		water_id -- id corresponding to the water body being placed
		'''

		i = 0

		from __import__ import Water

		# allowed = False
		tmp_list = []

        # create random x and y for water body
		y = numpy.random.uniform((numpy.sqrt((self.water_prev
											* self.width * self.height) * 4)), \
			numpy.sqrt(self.water_prev * self.width * self.height)) / nr_water

		x = ((self.water_prev * self.width * self.height) / y) / nr_water

		size = {'width': x, 'height': y}

		index = i

		new_water = Water(index, size)

		tmp_list.append(new_water)

		i += 1

        #check if ratio is correct
		if ((x / y) < 0.25) & ((x / y) > 4):
			return False

		for water in self.water:

			# check if corner is not inside other water body
			for c in new_water.corners:

				if (new_water.corners[c]['x'] >= water.corners['lb']['x'] and
					new_water.corners[c]['x'] <= water.corners['rb']['x'] and
				    new_water.corners[c]['y'] <= water.corners['lb']['y'] and
				    new_water.corners[c]['y'] >= water.corners['lo']['y']):

					# stop function if there is overlap
					return False

			for c in water.corners:

				if (water.corners[c]['x'] >= new_water.corners['lb']['x'] and
					water.corners[c]['x'] <= new_water.corners['rb']['x'] and
				    water.corners[c]['y'] <= new_water.corners['lb']['y'] and
				    water.corners[c]['y'] >= new_water.corners['lo']['y']):

					# stop function if there is overlap
					return False

        # check if water is on map
		for water in tmp_list:
			if water.corners['lo']['x'] > 0 and water.corners['lo']['y'] > 0 \
			and water.corners['lb']['x'] > 0 and water.corners['lb']['y'] < self.height \
			and water.corners['ro']['x'] < self.width and water.corners['ro']['y'] > 0 \
			and water.corners['rb']['x'] < self.width and water.corners['rb']['y'] < self.height:
				self.water.append(water)
				return True


	def place_water(self, index, nr_water):

		from __import__ import House, MAP_20

        # create dummy house
		d_house = House(100,MAP_20['types_houses'][0], None)

		self.construction.append(d_house)

		tmp_list = []

		# get location with max freespace
		fpm = self.calc_freespace_on_map()

        # initialize last location
		j = len(fpm[1]) - 1
		del self.construction[0]

        # calculate total water body
		area = (self.water_prev * self.width * self.height)

		while len(self.water) < 4: #and area =! 0

			j = j - i

			# get best location from freespace_on_map
			best_loc = fpm[0][j]

            # get min freespace for best_loc[j]
			freespace_len = fpm[1][j]

			# multiply the minimal freespace to get total water body
			width = freespace_len * 2
			height = freespace_len * 2

			size = {'width': width, 'height': height}

			new_water = Water(index, size, best_loc)

			tmp_list.append(new_water)

			if ((width / height) < 0.25) & ((width / height) > 4):
				return False

			for water in self.water:

				# check if corner is not inside other water body
				for c in new_water.corners:

					if (new_water.corners[c]['x'] >= water.corners['lb']['x'] and
						new_water.corners[c]['x'] <= water.corners['rb']['x'] and
					    new_water.corners[c]['y'] <= water.corners['lb']['y'] and
					    new_water.corners[c]['y'] >= water.corners['lo']['y']):

						# stop function if there is overlap
						return False

				for c in water.corners:

					if (water.corners[c]['x'] >= new_water.corners['lb']['x'] and
						water.corners[c]['x'] <= new_water.corners['rb']['x'] and
					    water.corners[c]['y'] <= new_water.corners['lb']['y'] and
					    water.corners[c]['y'] >= new_water.corners['lo']['y']):

						# stop function if there is overlap
						return False

            # check if water is on map
			for water in tmp_list:
				if water.corners['lo']['x'] > 0 and water.corners['lo']['y'] > 0 \
				and water.corners['lb']['x'] > 0 and water.corners['lb']['y'] < self.height \
				and water.corners['ro']['x'] < self.width and water.corners['ro']['y'] > 0 \
				and water.corners['rb']['x'] < self.width and water.corners['rb']['y'] < self.height:
					self.water.append(water)
					return True

	def calc_freespace_on_map(self):
		'''Calculating location with the most freespace on map. '''

		# Input arguments:
		# new_house --  house that is being moved


		# initiate possible freespace variable
		poss_freespace = 0

		coordinates = []

		fp = []

		# iterate over map width
		for i in range(5, self.width, 5):



			# iterate over map height
			for j in range(5, self.height, 5):

				# place house on i,j location
				allowed = self.place_house(0, {'x' : i, 'y' : j})


				if allowed == True:

					# store the possible freespace of new location
					if (self.houses[len(self.houses) - 1].calc_freespace(self) != False):

						# store freespace in tmp
						tmp = self.houses[len(self.houses) - 1].freespace

						# if new freespace is greater then update
						if (tmp >= poss_freespace):

							# update new possible freespace
							poss_freespace = tmp

							fp.append(poss_freespace)

							# update location of possible freespace
							coordinates.append({'x' : i, 'y' : j})

					# remove house that is placed
					self.remove_house(len(self.houses) - 1)

		# return coordinates
		return [coordinates, fp]

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
			self.remove_house(tmp_index[i])

		# add same amount of houses which were deleted
		# for i in range(nr_houses):

			allowed = False

			while allowed == False:

				loc = {'x' : numpy.random.uniform(0, self.height),
					   'y' : numpy.random.uniform(0, self.width)}

				allowed = self.place_house(i, loc)


	def tactical_swap_houses(self, nr_houses):
		''' Moves, every iteration, three houses for optimalization.

		Input arguments:
		in_map -- input map
		nr_houses -- nr of houses swapped
		'''

		# iterate over amount of swaps
		for i in range(nr_houses):

			# remove the first house
			self.remove_house(0)

			allowed = False

			# get freespace coordinates on map
			coordinates = self.calc_freespace_on_map(self.construction[0])

			j = len(coordinates[0]) - 1

			# place house where valid beginning with biggest freespace to smallest
			while (allowed == False):

				allowed = self.place_house(0, coordinates[0][j])

				j += -1


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
