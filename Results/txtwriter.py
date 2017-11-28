# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

def save_results(results, filename):
	'''Saves results to text file 

	Input arguments:
	results -- a list stored with results
	filename -- a string as outputname for the file
	'''

	filename = open(filename + '.txt', 'w')

	for item in results:
		filename.write("%s\n" % item)
