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


	name = open(string + 'Results' + split + directory + split +
					name + '.txt', 'w')

	for item in results:
		name.write("%s\n" % item)
