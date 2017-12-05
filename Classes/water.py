# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

class Water_Element(object):
	'''Class for water object.'''

	def __init__(self, loc):
		'''Class is list of coordinates on where the water is placed.

		Input arguments:
		loc -- location where water is placed
		'''

		self.location = loc
		self.size = ''