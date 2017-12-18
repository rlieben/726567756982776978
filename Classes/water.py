# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns


import random

class Water(object):
	'''Class for water object.'''

	def __init__(self, self_id, size, loc):
		'''Creates object of class Water.

		Input arguments:
		self_id -- int, individual identification number
		size -- dict of floats, containing width and height of element
		loc -- dict of floats, location of water element
		'''

		self.self_id = self_id
		self.width = size['width']
		self.height = size['height']
		self.location = loc

		# !!!!!!!!!!!!!!!!!!!!!!
		self.corners = self.find_corners()


	def find_corners(self):
		'''Calculates coordinates of corners.

		Returns dictionary containing:
		lb -- coordinate of the top left corner
		rb -- coordinate of the top right corner
		lo -- coordinate of the lower left corner
		ro -- coordinate of the lower right corner
		'''

		lb = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		rb = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		lo = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		ro = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		return {'lb' : lb, 'rb': rb, 'lo': lo, 'ro': ro}
