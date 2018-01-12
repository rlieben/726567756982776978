# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


import sys


def save_results(results, directory, name):
	'''Saves results to text file in given directory

	Input arguments:
	results -- list, containing scores
	directory --  directory -- string, name of directory in results
	name -- string, name of outputfile
	'''

	from __import__ import string, split

	# open file with specified name
	name = open(string + 'Results' + split + directory + split +
					name + '.txt', 'w')

	# write results to file
	for item in results:
		name.write("%s\n" % item)


def csv_writer(steps, directory, name):

	from __import__ import string, split

	self_id = open(string + 'Data_Project' + split + directory + split +
				   'self_id' + name + '.csv', 'w')
	size = open(string + 'Data_Project' + split + directory + split +
				'size' + name + '.csv', 'w')
	location = open(string + 'Data_Project' + split + directory + split +
				    'location' + name + '.csv', 'w')
	value = open(string + 'Data_Project' + split + directory + split +
				 'value' + name + '.csv', 'w')
	freespace = open(string + 'Data_Project' + split + directory + split +
				     'freespaces' + name + '.csv', 'w')
	neighbour = open(string + 'Data_Project' + split + directory + split +
				      'neighbours' + name + '.csv', 'w')
	self_type = open(string + 'Data_Project' + split + directory + split +
				     'type' + name + '.csv', 'w')

	for step in steps:

		for house in step.houses:

			tmp_fs = []
			tmp_nb = []

			for i in range(len(house.neighbours)):
				if house.neighbours[i] not in tmp_nb:
					tmp_nb.append(house.neighbours[i])
					tmp_fs.append(house.freespaces[i])

			self_id.write("%s," % house.self_id)
			size.write("%s;" % house.width)
			size.write("%s," % house.height)
			location.write("%s," % house.location)
			value.write("%s," % house.value)
			for fs in tmp_fs:
				freespace.write("%s; " % fs)
			freespace.write(", ")
			for nb in tmp_nb:
				neighbour.write("%s; " % nb)
			neighbour.write(", ")
			self_type.write("%s," % house.type)


		self_id.write("\n")
		size.write("\n")
		location.write("\n")
		value.write("\n")
		freespace.write("\n")
		neighbour.write("\n")
		self_type.write("\n")
