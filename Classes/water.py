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
		self_id -- intiger, individual identification number
		size -- dict of floats, containing width and height of element
		loc -- dict of floats, location where water is placed
		'''

		self.self_id = self_id
		self.width = size['width']
		self.height = size['height']
		self.location = loc
		self.corners = self.find_corners()


	def find_corners(self):
		'''Calculates coordinates of corners.

		Output argument:
		dict of dicts, containing coordinates of corners'''

		lb = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		rb = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		lo = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		ro = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		return {'lb' : lb, 'rb': rb, 'lo': lo, 'ro': ro}
