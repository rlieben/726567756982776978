# Study:        Minor Programming, University of Amsterdam
# Course:       Heuristics
# Assignment:   Amstelhaege
# Group:        726567756982776978
# Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

import pip

def install(packages):

    '''Installation of all required packages and requirements.

    Input arguments:
    packages -- list of strings, packages which need to be installed
    '''

    for package in packages:
        print('installing: ', package)
        pip.main(['install', package])

if __name__ == '__main__':
    install(['seaborn', 'matplotlib', 'numpy', 'imageio'])
