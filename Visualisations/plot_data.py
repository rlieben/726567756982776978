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
    plt.figure(figsize=(20,10))

    if len(data) > 1:
        for list in data:
            plt.plot(list)
    else:
        plt.plot(data)

    plt.ylabel('score(€)')
    plt.xlabel('# of maps')

    find_forward = sys.path[0].find('/')
    find_backward = sys.path[0].find('\\')

    if find_forward > find_backward:
        split = '/'
    else:
        split = '\\'

    list_dir = sys.path[0].split(split)
    string = ''
    for i in range(len(list_dir) - 1):
        string += list_dir[i]
        string += split

    plt.savefig(string + 'Results' + split + directory + split + name
    			 + '.png')
