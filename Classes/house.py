# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import numpy

class House(object):
	'''Basis for the three different house classes.'''

	def __init__(self, self_id, house_charac, loc):
		'''Creates object of class house.

		Input arguments:
		type_charac -- dict containing characteristics of house type_charac
		loc -- location of house
		'''

		self.width = house_charac['width']
		self.height = house_charac['height']
		self.start_value = house_charac['start_value']
		self.perc = house_charac['perc']
		self.min_free = house_charac['min_free']
		self.type = house_charac['type']
		self.index_nr = house_charac['index']
		self.colour = house_charac['colour']

		self.self_id = self_id
		self.location = loc # loc is a dict {'x' : ..., 'y' : ...}
		self.corners = None
		self.freespace = None
		self.value = None
		self.direction = None



	def calc_value(self):
		'''Calculates the value of this house.'''


		value = self.start_value + (self.start_value
				* (self.freespace - self.min_free)
				* self.perc)

		self.value = value
		return value



	def find_corners(self):
		'''Calculates coordinates of corners.'''

		lb = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		rb = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		lo = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		ro = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		self.corners = {'lb' : lb, 'rb': rb, 'lo': lo, 'ro': ro}


	def calc_freespace(self, in_map):
		'''Calculates freespace of the house.

		Input arguments:
		in_map -- map where the house is placed on
		'''

		# initiate list for possible freespaces
		tmp_freespace = []

		tmp_direction = []

		# initiate lists for other houses, based on orientation to this house
		tmp_range_x = []
		tmp_range_y = []
		tmp_range_c = []

		# add distances to sides of map to list of freespaces
		for c in self.corners:

			diff_l = self.corners['lb']['x']
			diff_r = self.corners['rb']['x'] - in_map.width
			diff_b = self.corners['lb']['y'] - in_map.height
			diff_o = self.corners['lo']['y']

			tmp_freespace.append(abs(diff_l))
			tmp_freespace.append(abs(diff_r))
			tmp_freespace.append(abs(diff_b))
			tmp_freespace.append(abs(diff_o))

			tmp_direction.append({'x' : diff_l, 'y' : 0})
			tmp_direction.append({'x' : diff_r, 'y' : 0})
			tmp_direction.append({'x' : 0, 'y' : diff_b})
			tmp_direction.append({'x' : 0, 'y' : diff_o})

		# iterate over houses build on map
		for house in in_map.houses:

			# skip itself
			if house.self_id != self.self_id:

				# if other house is above or below this house, add to y list
				if ((house.corners['lb']['x'] >= self.corners['lb']['x'] and
					 house.corners['lb']['x'] <= self.corners['rb']['x']) or
				    (house.corners['rb']['x'] >= self.corners['lb']['x'] and
				     house.corners['rb']['x'] <= self.corners['rb']['x'])):

					tmp_range_y.append(house)

				# if other house is left or right of this house, add to x list
				elif ((house.corners['lb']['y'] >= self.corners['lo']['y'] and
					   house.corners['lb']['y'] <= self.corners['lb']['y']) or
				      (house.corners['lo']['y'] >= self.corners['lo']['y'] and
				       house.corners['ro']['y'] <= self.corners['lb']['y'])):

					tmp_range_x.append(house)

				# otherwise, other house must closest to corner
				else:

					tmp_range_c.append(house)


		# add distance in terms of x to list of freespaces
		for house in tmp_range_x:

			# calculate for other house left and right
			diff_l = self.corners['lb']['x'] - house.corners['rb']['x']
			diff_r = self.corners['rb']['x'] - house.corners['lb']['x']

			tmp_freespace.append(abs(diff_l))
			tmp_freespace.append(abs(diff_r))

			tmp_direction.append({'x' : diff_l, 'y' : 0})
			tmp_direction.append({'x' : diff_r, 'y' : 0})


		# add distance in terms of y to list of freespaces
		for house in tmp_range_y:

			# calculate for other house above and below
			diff_b = self.corners['lb']['y'] - house.corners['lo']['y']
			diff_o = self.corners['lo']['y'] - house.corners['lb']['y']

			tmp_freespace.append(abs(diff_b))
			tmp_freespace.append(abs(diff_o))

			tmp_direction.append({'x' : 0, 'y' : diff_b})
			tmp_direction.append({'x' : 0, 'y' : diff_o})


		# add distance between corners to list of freespaces
		for house in tmp_range_c:

			# iterate over all corners of other house
			for c1 in house.corners:

				# iterate over all corners of this house
				for c2 in self.corners:

					diff_x = self.corners[c2]['x'] - house.corners[c1]['x']
					diff_y = self.corners[c2]['y'] - house.corners[c1]['y']

					diff = numpy.sqrt(numpy.power(diff_x, 2) +
									  numpy.power(diff_y, 2))

					tmp_freespace.append(abs(diff))

					tmp_direction.append({'x' : diff_x, 'y' : diff_y})

		index = numpy.argmin(tmp_freespace)
		self.freespace = tmp_freespace[index]
		self.direction = tmp_direction[index]
