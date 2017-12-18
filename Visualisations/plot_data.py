# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns


import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import seaborn as sns


def plot_data(data, directory, name):
    '''Creates plot of input data in given directory.

    Input arguments:
    data -- list, input data
    directory -- string, name of directory in results
    name -- string, name of outputfile
    '''

	# set background style and figure size
    sns.set_style('darkgrid')
    plt.figure(figsize = (20, 10))

	# init list for legend en name
    legend_list = []
    run = 0

	# add every list of data to graph and legend
    for list in data:
        run += 1
        plt.plot(list)
        legend_list.append(run)

	# create text y and x axes
    plt.ylabel('Score(€)')
    plt.xlabel('Iterations')

	# add legend
    plt.legend(legend_list)

    from __import__ import string, split

	# save to directory with name
    plt.savefig(string + 'Results' + split + directory + split + name
    			 + '.png')
