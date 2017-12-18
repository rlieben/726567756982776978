# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holte, Raoul Lieben, Luc Stefelmanns

import matplotlib as mpl
import matplotlib.pyplot as plt
import sys


def plot_data(data, directory, name):
    '''Creates plot of input data in given directory.

    Input arguments:
    data -- list, input data
    directory -- string, name of directory in results
    name -- string, name of outputfile
    '''
    plt.figure(figsize=(20,10))
    legend_list = []
    run = 0

    for list in data:
        run += 1
        plt.plot(list)
        legend_list.append(run)

    plt.ylabel('score(€)')
    plt.xlabel('# of maps')
    plt.legend(legend_list)

    from __import__ import string, split

    plt.savefig(string + 'Results' + split + directory + split + name
    			 + '.png')
