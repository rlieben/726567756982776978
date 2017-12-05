# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

class Water_Element(object):
	'''Class for water object.'''

	def __init__(self, loc, self_id, size):
		'''Class is list of coordinates on where the water is placed.

		Input arguments:
		loc -- location where water is placed
		'''

		self.location = loc
		self.self_id = self_id
		self.width = size['width']
		self.height = size['height']
		self.corners = self.find_corners_water()


	def find_corners_water(self):
		'''Calculates coordinates of corners. '''

		lb = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		rb = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] + 0.5 * self.height)}

		lo = {'x' : (self.location['x'] - 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		ro = {'x' : (self.location['x'] + 0.5 * self.width),
			  'y' : (self.location['y'] - 0.5 * self.height)}

		return {'lb_w' : lb, 'rb_w': rb, 'lo_w': lo, 'ro_w': ro}
