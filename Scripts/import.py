import sys
list_dir = sys.path[0].split('\\')
string = ''
for i in range(len(list_dir) - 1):
    string += list_dir[i]
    string += '\\'

string += 'Archive'

sys.path.insert(0, string)

from export import *

function()
