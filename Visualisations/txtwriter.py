# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

import sys

def save_results(results, directory, filename):
	'''Saves results to text file

	Input arguments:
	results -- list, containing scores
	filename -- string, outputname for the file
	'''

	from __import__ import string, split


	filename = open(string + 'Results' + split + directory + split +
					filename + '.txt', 'w')

	for item in results:
		filename.write("%s\n" % item)
