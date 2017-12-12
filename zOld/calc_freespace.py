
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
