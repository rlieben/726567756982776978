# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

import sys

def save_results(results, filename):
	'''Saves results to text file

	Input arguments:
	results -- a list stored with results
	filename -- a string as outputname for the file
	'''

	find_forward = sys.path[1].find('/')
	find_backward = sys.path[1].find('\\')

	if find_forward > find_backward:
		split = '/'
	else:
		split = '\\'

	list_dir = sys.path[1].split(split)
	string = ''
	for i in range(len(list_dir)):
	    string += list_dir[i]
	    string += split


	filename = open(string + 'Results' + split + filename + '.txt', 'w')

	for item in results:
		filename.write("%s\n" % item)
