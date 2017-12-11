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

		self.self_id = self_id
		self.location = loc # loc is a dict {'x' : ..., 'y' : ...}
		self.corners = self.find_corners()
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
		'''Calculates coordinates of corners. '''

		lb = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		rb = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		lo = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		ro = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		return {'lb' : lb, 'rb': rb, 'lo': lo, 'ro': ro}


	def calc_freespace(self, in_map):
		'''Calculates freespace of the house.

		Input arguments:
		in_map -- map where the house is placed on
		'''
		# coordinates new house
		x_newhouse = self.location['x']
		y_newhouse = self.location['y']

		# initiate variable list
		diff_houses = [0, 0]

		# difference between center and wall of new house
		x_diffwall = self.width / 2
		y_diffwall = self.height / 2

		# creating temporary variable for freespace
		tmpfreespace = []

		# calculating distance to borders and adding to tmp freespace
		if (x_newhouse - x_diffwall < 0) or \
		   (y_newhouse - y_diffwall < 0) or \
		   (in_map.width - x_newhouse - x_diffwall < 0) or \
		   (in_map.height - y_newhouse - y_diffwall < 0):
		 	return False
		tmpfreespace.append(abs(x_newhouse - x_diffwall))
		tmpfreespace.append(abs(y_newhouse - y_diffwall))
		tmpfreespace.append(abs(in_map.width - x_newhouse - x_diffwall))
		tmpfreespace.append(abs(in_map.height - y_newhouse - y_diffwall))

        # check if house is not located in water
		# if self.corners['lb']['y'] > in_map.water.corners['lo']['y'] or \
		#    self.corners['lo']['x'] < in_map.water.corners['ro']['x'] or \
		#    self.corners['lo']['y'] < in_map.water.corners['lb']['y'] or \
		#    self.corners['ro']['x'] > in_map.water.corners['lo']['x']:
		#    	return False

		# iterate over all houses in map
		for house in in_map.houses:

			# skips itself
			if house.self_id != self.self_id:

				diff_houses[0] = abs(house.location['y'] - self.location['y'])
				diff_houses[1] = abs(house.location['x'] - self.location['x'])

				# check if coordinate falls within house x - range
				if house.corners['lb']['x'] > self.corners['lb']['x'] \
				   and house.corners['lb']['x'] < self.corners['rb']['x']:

				   	# check if no overlap
					if diff_houses[0] - x_diffwall - (house.width / 2) < 0:
						return False

					# save freespace between walls of houses
					tmpfreespace.append(diff_houses[0] \
										- x_diffwall
										- (house.width / 2))

					# check if coordinate falls within house y - range
					if house.corners['lo']['y'] > self.corners['lo']['y'] \
						 and house.corners['lo']['y'] < self.corners['lb']['y']:

						# check if no overlap
						if diff_houses[1] - y_diffwall - (house.width / 1) < 0:
							return False

						# save freespace between walls of houses
						tmpfreespace.append(abs(diff_houses[1] \
											- y_diffwall
											- (house.height / 2)))

				# check if coordinate falls within house y - range
				elif house.corners['lo']['y'] > self.corners['lo']['y'] \
					 and house.corners['lo']['y'] < self.corners['lb']['y']:

					# check if no overlap
					if diff_houses[1] - y_diffwall - (house.width / 1) < 0:
						return False

					# save freespace between walls of houses
					tmpfreespace.append(abs(diff_houses[1] \
										- y_diffwall
										- (house.height / 2)))

					# check if coordinate falls within house x - range
					if house.corners['lb']['x'] > self.corners['lb']['x'] \
				   		and house.corners['rb']['x'] < self.corners['rb']['x']:

				   		# check if no overlap
						if diff_houses[0] - x_diffwall - (house.width / 2) < 0:
							return False

						# save freespace between walls of houses
						tmpfreespace.append(diff_houses[0] \
											- x_diffwall
											- (house.width / 2))

				# else compute distance of corners of the house
				else:

					# create corner variable
					diff_corners = [0,0]

					# create distance variable list
					distancelist = []

					# iterate over corners of both houses
					for i in self.corners:

						for j in house.corners:

							# calculate x and y difference between corners
							diff_corners[0] = abs(self.corners[i]['x'] \
											  	  - house.corners[j]['x'])

							diff_corners[1] = abs(self.corners[i]['y'] \
											  	  - house.corners[j]['y'])

							# calculates distance between curr two corners
							distancecorn = abs(numpy.sqrt(numpy.power( \
													  diff_corners[0], 2) \
													  + numpy.power( \
													  diff_corners[1], 2)))
							# save distance
							distancelist.append(distancecorn)
						# take the minimum distance
						tmpfreespace.append(numpy.amin(distancelist))
				# take the minimum freespace
		self.freespace = numpy.amin(tmpfreespace)
