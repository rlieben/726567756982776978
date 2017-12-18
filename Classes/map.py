# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import copy
import numpy

class Map(object):
	'''List that keeps track of all the houses and water.'''

	def __init__(self, map_specs):
		'''Creates map.

		Input arguments:
		map_specs -- dict containing:
			width -- float, width of map
			height -- float, height of map
			nr_waterbodies -- int, maximal number of water bodies allowed
			water_prev -- float, fraction of map that must be covered by water
			types_houses -- list containing specifications of house types

		Example: Map(MAP_20)
		'''

		self.width = map_specs['width']
		self.height = map_specs['height']
		self.max_waterbodies = map_specs['nr_waterbodies']
		self.water_prev = map_specs['water_prev']
		self.types_houses = map_specs['types_houses']

		# list containing all houses that have been placed
		self.houses = []

		# list containing all water elements
		self.water = []

		# list containing all houses that have not been placed
		self.construction = self.create_construction(map_specs)

		# calculated with calc_score
		self.score = None



	def create_construction(self, map_specs):
		'''Creates list of houses that need to be placed.

		Input arguments:
		map_specs -- dict, see docstrings __init__

		Returns list of objects, containing houses
		'''

		from __import__ import House

		# initialize variable, location and empty list
		house_id = 0
		loc = {'x' : None, 'y' : None}
		construction = []

		# iterate over distribution and number of houses
		for i in range(len(map_specs['distr_houses'])):
			for j in range(int(map_specs['distr_houses'][i]
						   	   * map_specs['nr_houses'])):

				# append houses to construction list
				construction.append(House(house_id,
										  map_specs['types_houses'][i], loc))
				house_id += 1

		return construction


	def rand_loc_water(self):
		'''Generates random location for water

		Returns dict of floats, a coordinate for the water
		'''

		loc = {'x' : random.uniform((0 + 0.5 * water.width), \
				  					(self.width - 0.5 * water.width)), \
			   'y' : random.uniform((0 + 0.5 * water.height), \
		  							(self.height - 0.5 * water.height))}

		return loc


	def place_house(self, index, loc):
		'''Places house on the map.

		Input:
		index -- int, index number of house in construction list
		loc -- dict of floats, location

		Updates:
		self.construction -- object, remove house that is placed
		self.houses -- object, adds house that is placed

		Example: map.place_house(0, {'x' : 10, 'y' : 11})
		'''

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
		''' Removes house.

		Input:
		index -- int, index of house in list self.houses

		Updates:
		self.houses -- object, removes house from list
		self.construction -- object, adds house to list

		Example: map.remove_house(3)
		'''

		# copies house
		tmp_house = copy.copy(self.houses[index])

		# resets all specific values of this house on this map
		tmp_house.location = {'x' : None, 'y' : None}
		tmp_house.freespace = None
		tmp_house.value = None

		# adds house to construction list and deletes from houses list
		self.construction.append(tmp_house)
		del self.houses[index]


	def place_water_random(self):
		'''Places random water on the map, number of elements is maximum of map.

		Update:
		self.water -- object, newly placed water elements
		'''

		from __import__ import Water

		# initializes variable and empty list
		i = 0
		tmp_list = []

		# allowed = False


        # create random x and y for water body
		y = numpy.random.uniform((numpy.sqrt((self.water_prev
										    * self.width * self.height) * 4)), \
			numpy.sqrt(self.water_prev * self.width * self.height)) \
			/ self.max_waterbodies

		x = ((self.water_prev * self.width * self.height) / y) \
			/ self.max_waterbodies

		# sets size of waterbody
		size = {'width': x, 'height': y}

		index = i

		# sets random location for waterbody
		loc = {'x' : numpy.random.uniform((0 + 0.5 * x), \
				  	(self.width - 0.5 * x)), \
			   'y' : numpy.random.uniform((0 + 0.5 * y), \
		  			(self.height - 0.5 * y))}

		# creates new water element and appends to list
		new_water = Water(index, size, loc)
		tmp_list.append(new_water)

        #check if ratio is correct
		if ((x / y) < 0.25) & ((x / y) > 4):
			return False

		# iterate over water bodies
		for water in self.water:

			# check if location falls between walls
			if (new_water.location['x'] > water.corners['lb']['x'] and
				new_water.location['x'] < water.corners['rb']['x'] and
				new_water.location['y'] > water.corners['lo']['y'] and
				new_water.location['y'] < water.corners['lb']['y']):
				return False

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
			if water.corners['lo']['x'] > 0 and \
			    water.corners['lo']['y'] > 0 and \
			    water.corners['lb']['x'] > 0 and \
			    water.corners['lb']['y'] < self.height and \
			    water.corners['ro']['x'] < self.width and \
			    water.corners['ro']['y'] > 0 and \
			    water.corners['rb']['x'] < self.width and \
			    water.corners['rb']['y'] < self.height:

				self.water.append(water)

				return True


	def place_water(self):
		'''Places water on the map after placing houses.
		'''

		from __import__ import House, Water

        # create dummy house
		d_house = House(100, self.types_houses[0], None)

		self.construction.append(d_house)

		tmp_list = []

		# get location with max freespace
		freespace_listm = self.calc_freespace_on_map(5)

        # initialize last location
		j = len(freespace_listm[1]) - 1
		i = 0
        # calculate total water body
		area = (self.water_prev * self.width * self.height)

		for i in range(self.max_waterbodies):

			j = j - i

			print(i)

			# get best location from freespace_on_map
			best_loc = freespace_listm[0][j]

		    # get min freespace for best_loc[j]
			freespace_len = freespace_listm[1][j]

			# multiply the minimal freespace to get total water body
			width = freespace_len * 2
			height = freespace_len * 2

			print(width,height)

			size = {'width': width, 'height': height}

			new_water = Water(j, size, best_loc)

			self.water.append(new_water)

			i -= 1

		del self.construction[0]



	def calc_freespace_on_map(self, iterationstep):
		'''Calculating location with the most freespace on map.

		Input:
		iterationstep -- integer, size of iteration step through the map

		Returns:
		coordinates -- list of dicts, which are coordinates of floats
		'''

		# initiate variable and empty lists for coordinates
		poss_freespace = 0
		coordinates = []

		# iterate over map width
		for i in range(iterationstep, self.width, iterationstep):

			# iterate over map height
			for j in range(iterationstep, self.height, iterationstep):

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

							# update location of possible freespace
							coordinates.append({'x' : i, 'y' : j})

					# remove house that is placed
					self.remove_house(len(self.houses) - 1)

		return coordinates


	def random_swap_houses(self, nr_houses):
		'''Moves, every iteration, a house for optimalization.

		Input:
		nr_houses -- int, number of houses to swap randomly

		Update:
		self.houses -- object, changes location of houses in list
		'''

		# initializes empty lists for index and houses
		tmp_index = []
		tmp_houses = []

		# iteraters over houses and removes them
		for i in range(nr_houses):
			tmp_index.append(int(numpy.random.uniform(0, len(self.houses) - 1)))
			tmp_houses.append(self.houses[tmp_index[i]])
			self.remove_house(tmp_index[i])

		# add same amount of houses which were deleted
		for i in range(nr_houses):

			allowed = False

			while allowed == False:

				loc = {'x' : numpy.random.uniform(0, self.height),
					   'y' : numpy.random.uniform(0, self.width)}

				allowed = self.place_house(i, loc)


	def tactical_swap_houses(self, nr_houses):
		''' Moves, every iteration, houses for optimalization.

		Input:
		nr_houses -- int, number of houses to swap with greedy tactics

		Update:
		self.houses -- object, changes location of houses in list
		'''

		# iterate over amount of swaps
		for i in range(nr_houses):

			# remove the first house
			self.remove_house(0)

			allowed = False

			# get freespace coordinates on map
			coordinates = self.calc_freespace_on_map(5)

			j = len(coordinates) - 1

			# place house where valid beginning with biggest freespace to smallest
			while (allowed == False):

				allowed = self.place_house(0, coordinates[j])

				j += -1


	def calc_score(self):
		'''Calculates score of map.

		Returns:
		summy -- float, score of map

		Updates:
		self.score -- float, score of map
		'''

		# intializes variable
		summy = 0

		# iterates over houses and sums each score
		for house in self.houses:
			house.calc_freespace(self)
			house.calc_value()
			summy += house.value

		self.score = summy
		return summy
