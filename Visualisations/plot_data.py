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
    '''Creates plot of input data.

    Input arguments:
    data -- list, input data
    directory -- string, name of directory in results
    name -- string, name of outputfile
    '''
    sns.set_style('darkgrid')
    plt.figure(figsize=(20,10))
    legend_list = []
    run = 0

    for list in data:
        run += 1
        plt.plot(list)
        legend_list.append(run)

    plt.ylabel('Score(€)')
    plt.xlabel('Iterations')
    plt.legend(legend_list)

    from __import__ import string, split

    plt.savefig(string + 'Results' + split + directory + split + name
    			 + '.png')
