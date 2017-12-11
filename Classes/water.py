# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

import random
from Classes.map import *
from Characteristics.Amstelhaege import *

class Water(object):
	'''Class for water object.'''

	def __init__(self, self_id, size):
		'''Class is list of coordinates on where the water is placed.

		Input arguments:
		loc -- location where water is placed
		'''

		self.self_id = self_id
		self.width = size['width']
		self.height = size['height']
		self.location = self.create_location()
		self.corners = self.find_corners()


	def find_corners(self):
		'''Calculates coordinates of corners. '''

		print (self.location)
		lb = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		rb = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		lo = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		ro = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		return {'lb' : lb, 'rb': rb, 'lo': lo, 'ro': ro}

	def create_location(self):
		'''generates location for water bodies '''

		loc = {'x' : random.uniform((0 + 0.5 * self.width), \
				  	(MAP_20['width'] - 0.5 * self.width)), \
			   'y' : random.uniform((0 + 0.5 * self.height), \
		  			(MAP_20['height'] - 0.5 * self.height))}

		return loc
