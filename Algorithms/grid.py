# import matplotlib.pyplot as plt
# from matplotlib import colors
# import numpy as np
#
# data = np.random.rand(10, 10) * 20
#
# # create discrete colormap
# cmap = colors.ListedColormap(['red', 'blue'])
# bounds = [0,160,160]
# norm = colors.BoundaryNorm(bounds, cmap.N)
#
# fig, ax = plt.subplots()
# ax.imshow(data, cmap=cmap, norm=norm)
#
# # draw gridlines
# ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
# ax.set_xticks(np.arange(-.5, 10, 1));
# ax.set_yticks(np.arange(-.5, 10, 1));
#
# plt.show()


def makeGrid(g):
    n = []
    for i in range(g):
        temp = []
        for j in range(g):
            temp.append(g[j][i])
        n.append(temp)
    return n

grid = makeGrid(8)
print(grid)
